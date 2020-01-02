from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import sys
import argparse
import json
from string import Template 
from io import BytesIO

deepspeechCommand = Template('deepspeech --model $model --lm $lm --trie $trie --audio $audio')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		self.send_response(200)
		self.end_headers()
		tmpFilename = "upload.wav"
		file = open(tmpFilename, "wb") # file to write to
		file.write(body)
		result = subprocess.run(["deepspeech", "--model",config['deepspeech']['model'],
		'--lm',config['deepspeech']['lm'],'--trie',config['deepspeech']['trie'],'--audio',tmpFilename],stdout=subprocess.PIPE)
		response = BytesIO()
		response.write(result.stdout)
		self.wfile.write(response.getvalue())	



# Parse Arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-c','--config', help="Path of the server configuration file", required=True)
args = parser.parse_args()

with open(args.config) as json_file:
	config = json.load(json_file)

# Open Web Server	
httpd = HTTPServer((config['server']['host'], config['server']['port']), SimpleHTTPRequestHandler)
httpd.serve_forever()
