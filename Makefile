prepare:
	pipenv install
	npm install
	npm run dev
	cp example.env .env

cleanup:
	rm -rf .git
