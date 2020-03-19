FROM registry.cn-hangzhou.aliyuncs.com/last911/openresty-python3.7
WORKDIR /data/wwwroot

COPY requirements.txt ./
RUN apt update && \ 
    pip install --upgrade -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

COPY ["www.conf", "/etc/openresty/vhosts/"]
COPY ["run.sh", "/usr/bin"]
COPY . .

CMD ["sh", "/usr/bin/run.sh"]
