HOST=http://test.host.ru
LOGIN=test_user_123
PASSWORD=test_password_123


run-tests:
	pytest --login $(LOGIN) --password $(PASSWORD) --host $(HOST)

run-tests-with-allure: clear-allure
	pytest --login $(LOGIN) --password $(PASSWORD) --host $(HOST) --alluredir=./allure-results
	make generate-allure

clear-allure:
	rm -rf ./allure-results/
	rm -rf ./allure-report/

generate-allure:
	allure generate -c ./allure-results -o ./allure-report
	allure serve