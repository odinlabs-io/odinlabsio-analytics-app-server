#  MIT License
#
#  Copyright (c) 2020 OdinLabs IO
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from urllib.parse import urlparse

import bokeh.resources as bokeh_resources
import shortuuid
from bokeh.util.token import generate_session_id
from flask import Flask


def server_session(dashboard_id,
                   analytic_id,
                   url='http://localhost:5006/bkapp',
                   relative_urls=False,
                   resources='default',
                   headers=None,
                   size=None):
    """ Return a script tag that embeds content from a specific existing session on
        a Bokeh server.

        This function is typically only useful for serving from a a specific session
        that was previously created using the ``bokeh.client`` API.

        Bokeh apps embedded using these methods will NOT set the browser window title.

        .. note::
            Typically you will not want to save or re-use the output of this
            function for different or multiple page loads.

        Args:
            dashboard_id:

            analytic_id:

            url (str, optional) :
                A URL to a Bokeh application on a Bokeh server (default: "default")

                If ``"default"`` the default URL ``{DEFAULT_SERVER_HTTP_URL}`` will be used.

            relative_urls (bool, optional) :
                Whether to use relative URLs for resources.

                If ``True`` the links generated for resources such a BokehJS
                JavaScript and CSS will be relative links.

                This should normally be set to ``False``, but must be set to
                ``True`` in situations where only relative URLs will work. E.g.
                when running the Bokeh behind reverse-proxies under certain
                configurations

            resources (str) : A string specifying what resources need to be loaded
                along with the document.

                If ``default`` then the default JS/CSS bokeh files will be loaded.

                If None then none of the resource files will be loaded. This is
                useful if you prefer to serve those resource files via other means
                (e.g. from a caching server). Be careful, however, that the resource
                files you'll load separately are of the same version as that of the
                server's, otherwise the rendering may not work correctly.

           headers (dict[str, str], optional) :
                A dictionary of key/values to be passed as HTTP Headers
                to Bokeh application code (default: None)

        Returns:
            A properties needed to embed content from a Bokeh Server.

            .. warning::
                It is typically a bad idea to re-use the same ``session_id`` for
                every page load. This is likely to create scalability and security
                problems, and will cause "shared Google doc" behavior, which is
                probably not desired.
                :param url:
                :param analytic_id:
                :param dashboard_id:
                :param headers:
                :param resources:
                :param relative_urls:
                :param size:


        """
    if headers is None:
        headers = {}

    url = _clean_url(url)

    app_path = _get_app_path(url)
    element_id = shortuuid.uuid()
    src_path = _src_path(url, element_id)

    src_path += _process_app_path(app_path)
    src_path += _process_relative_urls(relative_urls, url)
    src_path += _process_args(dashboard_id, analytic_id, size)
    src_path += _process_resources(resources)

    headers = dict(headers) if headers else {}

    tag = {
        'srcPath': src_path,
        'appPath': app_path,
        'elementId': element_id,
        'analyticId': analytic_id,
        'headers': headers,
    }

    return tag


def _process_args(dashboard_id, analytic_id, size):
    initial = '&dashboardId={}&analyticId={}'.format(dashboard_id, analytic_id)
    if size.get('maxX'):
        initial = initial + '&maxX={}'.format(size['maxX'])
    if size.get('minX'):
        initial = initial + '&minX={}'.format(size['minX'])
    if size.get('maxY'):
        initial = initial + '&maxY={}'.format(size['maxY'])
    if size.get('minY'):
        initial = initial + '&minY={}'.format(size['minY'])

    return initial


def _process_resources(resources):
    """ Return an argument to suppress normal Bokeh server resources, if requested.

    Args:
        resources ("default" or None) :
            If None, return an HTML argument to suppress default resources.

    Returns:
        str

    """
    if resources not in ("default", None):
        raise ValueError("`resources` must be either 'default' or None.")
    if resources is None:
        return "&resources=none"
    return ""


def _process_relative_urls(relative_urls, url):
    """ Return an absolute URL HTML argument to add to a Bokeh server URL, if
    requested.

    Args:
        relative_urls (book) :
            If false, generate an absolute URL to add.

        url (str) :
            The absolute URL to add as an HTML argument

    Returns:
        str

    """
    if relative_urls:
        return ""

    return "&bokeh-absolute-url=" + url


def _process_app_path(app_path):
    """ Return an app path HTML argument to add to a Bokeh server URL.

    Args:
        app_path (str) :
            The app path to add. If the app path is ``/`` then it will be
            ignored and an empty string returned.

    """
    if app_path == "/":
        return ""

    return "&bokeh-app-path=" + app_path


def _src_path(url, element_id):
    """ Return a base autoload URL for a given element ID

    Args:
        url (str) :
            The base server URL

        element_id (str) :
            The div ID for autoload to target

    Returns:
        str

    """

    return '{}/autoload.js?bokeh-autoload-element={}'.format(url, element_id)


def _get_app_path(url):
    """ Extract the app path from a Bokeh server URL

    Args:
        url (str) :

    Returns:
        str

    """
    app_path = urlparse(url).path.rstrip("/")
    if not app_path.startswith("/"):
        app_path = "/" + app_path
    return app_path


def _clean_url(url):
    """ Produce a canonical Bokeh server URL.

    Args:
        url (str)
            A URL to clean, or "default". If "default" then the
            ``BOKEH_SERVER_HTTP_URL`` will be returned.

    Returns:
        str

    """
    if url == 'default':
        url = bokeh_resources.DEFAULT_SERVER_HTTP_URL

    if url.startswith("ws"):
        raise ValueError("url should be the http or https URL for the server, not the websocket URL")

    return url.rstrip("/")


class BokehService:
    def __init__(self):
        self._bokeh_url = None

    def init_app(self, app: Flask):
        self._bokeh_url = app.config.get('BOKEH_URL')

    def get_server_session(self, dashboard_id: str, analytic_id: str, args: dict):
        headers = {'Bokeh-Session-Id': generate_session_id()}
        return server_session(dashboard_id=dashboard_id, analytic_id=analytic_id, headers=headers, size=args,
                              url=self._bokeh_url)
