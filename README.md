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

For instance if the response is

```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Create a file containing just this data:

21oiJOfV6P-JYmf6c2wpAwnt6H1Un9x29YbGuMaQcwk.Yn42xqH2zI4oaBR2aGwxIkhzdTOC4miAg61sGmafyuM

And make it available on your web server at this URL:
```

the challenge used will be `Yn42xqH2zI4oaBR2aGwxIkhzdTOC4miAg61sGmafyuM`.

<br/>

```
export LE_CHALLENGES='LetsencryptChallengeToken'; python manage.py runserver 0.0.0.0:80
```
