---
title: bash shortcuts
date: 2019-12-13T01:30:00.000Z
tags: 'software, tips-and-tricks, bash'
---
tl;dr: bind common commands to shortcuts. save time. love life. cost: $0/mo or TODO with Alfred Powerpack read time: 15 minutes

TODO bash_profile explanation 

`cat ~/.bash_profile`

Exit vim `:wq` or ESC `:wq`

one line git push - ([GH origin](https://github.com/drj-io/gacp/blob/master/gacp))

```bash
#!/bin/bash
function gacp() {
    git add .
    git commit -a -m "$*"
    git push origin master
}
```

save without an extension as `gacp` (even tho it should be .sh) and `cp gacp /usr/local/bin`

Then you can quickly and easily commit and push with 

`gacp testing one-line commit push`

you may need to give yourself access to /usr/local/bin # TODO doesnt work in pipenv 

`sudo chown -R $(whoami) /usr/local/bin`

# general

`;genkey` Generate a random string of characters (for eg a password) 

`LC_ALL=C tr -dc 'A-Za-z0-9' </dev/random | head -c 30 ; echo`

 `;venv` General a virtual environment (you can also use `pipenv shell`) TODO check

```bash
virtualenv venv
source venv/bin/activate
```

Change director to bin `;bin` TODO explain what that is `cd /usr/bin`

`;delpyc` Delete cached python files (.pyc) 

`find . -name "*.pyc" -exec rm -rf {} \;`

`;countpy` Count Python Lines of Code (LoC) 

`wc -l $(git ls-files | grep '.*\.py')` 

I'll say for the record that LoC are generally a bad measure of anything, but they tend to be an understandable unit of measurement to non-technical folks

`;listlibs` Get a list of every installed library, ranked by size [Original SO thread](https://stackoverflow.com/questions/34266159/how-to-see-pip-package-sizes-installed):

```bash
pip3 list --format freeze|awk -F = {'print $1'}| xargs pip3 show | grep -E 'Location:|Name:' | cut -d ' ' -f 2 | paste -d ' ' - - | awk '{print $2 "/" tolower($1)}' | xargs du -sh 2> /dev/null|sort -h
```

Map the folder structure TODO

flake8 and black local folder TODO

## retcon? security? specific

 `;whois `Generic WHOIS TODO how to get a specific url into that  

`whois $(dig +short url.com | head -1)`

## github specific

`;ghauth`   Github Auth? TODO 

`ssh -vT git@github.com`

`;greset `Git reset soft  TODO explain  

`git reset --soft HEAD~1`

`;debugpush `Push an empty Git commit (for debugging, etc): 

```bash
git add .
git commit --allow-empty -m "Intentionally empty debug push"
git push origin master
```

`;dydesc`  

`aws dynamodb describe-table --table-name titleTable`

## flask specific

`;exportflask`  

`export FLASK_APP=FlaskApp.py`

`;runflask`  

`FLASK_APP=FlaskApp.py flask run`

`;debugflask`  

`export FLASK_DEBUG=1`

## django specific

`;debugfalse` `export heroku config:set DEBUG_MODE=False`

`;localdjango` Run localhost version of server `python3 manage.py runserver`

## heroku specific

`;hconfig` Show Heroku config, incl env vars 

`heroku config`

`;hkill` Restart a specific dyno 

`heroku restart worker.1`

`;hlog` Stream heroku logs 

`heroku logs -a app-name --tail`

`;hdb` SSH TODO? into heroku Postgres database 

`heroku pg:psql --app app-name`

`;hlocal` Run localhost version of Heroku server (http://0.0.0.0:5000/)

`heroku local web`

To create or update db tables - Migrate database (with particular db specified). At this point, Django created a file named 0001_initial.py inside the boards/migrationsdirectory.  You can list the migrations and their status with

`heroku run python3 manage.py makemigrations` 

`heroku run python3 manage.py migrate` 

`heroku run python manage.py showmigrations`