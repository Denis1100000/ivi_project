run-tests-allure:
	... --alluredir=./allure-results
	allure generate -c ./allure-results -o ./allure-report
	allure serve