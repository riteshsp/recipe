# recipe


for installation of elastic search use:
 https://stackoverflow.com/questions/39447617/failed-to-establish-a-new-connection-errno-111-connection-refusedelasticsear


install mysql client : 

apt install pkg-config
export MYSQLCLIENT_LDFLAGS=$(pkg-config --libs mysqlclient)
export MYSQLCLIENT_CFLAGS=$(pkg-config --cflags mysqlclient)
pip install mysqlclient --no-cache-dir