#Test
import os
import sys
import json
from utils import debug
import rekognize
import url
from flask import Flask, render_template, redirect, url_for, request, session
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy