# This is the API code I had from the previous instance.



# from flask import Flask, request, jsonify, render_template, redirect
# import os
# import json
# import pusher
# from database import db_session
# from models import Draft
# api = Flask(__name__)
#
# Team = [{'name' : 'Team Green'}, {'name' : 'Team Dostal'}, {'name' : 'Undrafted'}]
#
# #GET Players
# @api.route('/api/players')
# def index():
#      players = Draft.query.all()
#      return render_template('index.html', players=players)
#
# #GET Teams
# @api.route('/api/team')
# def team():
#     team = Draft.query.all()
#     return jsonify({'Team' : Team})
#
# #GET Players in Team Green
# @api.route('/api/team/<string:name>', methods=['GET'])
# def teamgreen(team):
#     tea = [team for team in Team if team['name'] == name]
#     return jsonify({'name' : tea[0]})
