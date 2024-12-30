- Opensource Job Portal developed using python, django framework with unlimited free job posting and Social Api's authentication.

## Recruiter

Recruiter can register using email or google login to post job.

- Can post jobs to social networking sites like facebook, twitter, linkedin.
- Walk-in's
- Copy An Existing Job Post, Deactivate.
- Add localtion in Google Maps
- Post their job to sociasudo usermod -aG docker $USERl networking sites.

## Portal

- Job Alerts
- New Mobile Design
- Normal Search and Advanced Search
- Email Notifications

### Useful tools and packages

```sh
pipdeptree # to see pip dependancy tree
black # to format code to meet python coding standards
pip-check -H  # to see upgradable packages
```

## Setup

Following are the setup instruction for ubuntu 20.04.

```

### Install and configure sass and less compilers

```bash
sudo gem install sass
```

You need to create symbolic link if you get error locating lessc
here my lessc file locatin is /usr/bin/lessc
you can find yours with this command `which lessc`

```bash
sudo ln -s /usr/bin/lessc /usr/local/bin/lessc
```

#### Install virtualenvwrapper

pip install virtualenvwrapper
add the following to your path

```export PATH="$PATH:/home/ubuntu/.local/bin"```
```source /home/ubuntu/.local/bin/virtualenvwrapper.sh```

##### Install requirements

```bash
pip install -r requirements.txt
```

For env variables, refer to env.md in source directory and you need to create a .env file to keep all env variables with their respective values.

##### Create db and import basic data to postgresql

sudo -u postgres psql

##### to change postgres password

ALTER USER postgres PASSWORD 'myPassword';

create database peeljobs
sudo -u postgres -i psql peeljobs < init_db/db_init.sql

##### Install docker and Run elasticsearch

to add user to docker group

```sudo usermod -aG docker $USER```
restart to apply changes.

```bash
```

##### Create index

Finally `update_index` command will freshen all of the content in your index. It iterates through all indexed models and updates the records in the index.

```bash
python manage.py update_index
```

##### Load data to postgres Database

Load data to cities, companies and etc using json files in "peeldb/fixtures" folder. please check below command for reference.

`python manage.py loaddata cities`
