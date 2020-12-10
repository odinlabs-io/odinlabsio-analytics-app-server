#TODO 

antl4
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar

add to .bashrc
export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'


antlr4 -Dlanguage=Python3 -o gen/ -listener -visitor Aggregation.g4

cd $project_dir

export PYTHONPATH=`pwd`/src ENV_CONF=`pwd`/config/app_config.py APP_CONF=app.settings_dev.DevelopmentConfig; gunicorn -w 4 gunicorn_app:app

export PYTHONPATH=`pwd`/src;python src/batch_app.py --csv data/nba_all_elo.csv --settings config.batch_config --generate-schema --batch app.batch.parquet_to_csv