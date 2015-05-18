BASE=$(pwd)
git clone https://github.com/cesanta/mongoose
cd mongoose/examples/web_server
git checkout -b https-decrypt-example c8e88e1710a1e20a0540f31c0a2897fa1d6aa480
make openssl

mkdir $BASE/webserver
cp web_server $BASE/webserver/web_server
cp certs/cert.pem $BASE/webserver/cert.pem
sed -n 19,46p cp certs/cert.pem > $BASE/webserver/private-key.pem
