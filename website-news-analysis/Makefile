#.PHONY: start

start: wsgi-stop wsgi-start
reload: wsgi-reload
stop: wsgi-stop
view-log: wsgi-view-log

##### wsgi 相關
wsgi-start:
	@echo "# wsgi 服務正在啟動 ..."
	@if [ -e /tmp/web-master.pid ]; then echo "# wsgi 服務已存在"; else pipenv run uwsgi --ini ./web/uwsgi.ini && echo "# wsgi 服務已啟動"; fi
wsgi-reload:
	@echo "# wsgi 服務正在重啟 ..."
	@if [ -e /tmp/web-master.pid ]; then pipenv run uwsgi --reload /tmp/web-master.pid && echo "# wsgi 服務已重啟"; else echo "# wsgi 服務未啟動"; fi
wsgi-stop:
	@echo "# wsgi 服務正在關閉 ..."
	@if [ -e /tmp/web-master.pid ]; then pipenv run uwsgi --stop /tmp/web-master.pid && echo "# wsgi 服務已關閉，等待五秒鐘 ..." && sleep 5; else echo "# wsgi 服務未啟動"; fi
wsgi-view-log:
	@echo "# 以下為 wsgi 服務的記錄檔 >>>>>>>>>>"
	@cat /var/log/uwsgi/web.log
	@echo "# 以上為 wsgi 服務的記錄檔 >>>>>>>>>>"
