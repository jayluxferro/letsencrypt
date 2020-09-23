### Letsencrypt - Domain Verification

### Development
**NB**: Python3

1. Clone project using git
```
git clone https://github.com/jayluxferro/letsencrypt
```

2. Navigate to project directory
```
cd letsencrypt
```

3. Install dependencies using pip
```
pip install -r requirements.txt 
```

4. Run local server
```
export LE_CHALLENGES='LetsencryptChallengeToken'; python manage.py runserver 0.0.0.0:80
```
