
from django.core import serializers
from rois.models import Label

def run(*args):

	with open(args[0],'r') as infile:
		for obj in serializers.deserialize('json',infile,ignorenonexistent=True):
			try:
             			obj.save()
			except Exception as e:
				print(str(e))
