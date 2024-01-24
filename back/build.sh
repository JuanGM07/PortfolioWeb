source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export 
unzip frontend.zip -d public
unzip backend.zip -d back
rm -f frontend.zip
rm -f backend.zip
deactivate