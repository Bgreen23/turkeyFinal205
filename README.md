# turkeyFinal205

This project is my 3rd semester software project. This will be a live draft table for a Turkeybowl Event.
The realtime-table folder is the pusher tutorial https://pusher.com/tutorials/live-table-flask that I based this off of.
##Initial Stories
As an Admin User, I need to be able to add players and teams
As an Admin User, I need to be able to add players to teams.
As an Admin User, I need to be able to update/edit the tables of teams and players.
As an Admin User, I need to be able to delete teams and players from the tables.
As an Admin User, I need to be able to assign player roles (Team Captain or Normal Player)
As an Admin User, I need to be able to log in.
As a Team Captain, I need to be able to draft players
As a User, I need to be able to view the draft table.
As a User, I should be able to add myself into the player table.

##Feature list:
  Create Database
  Create Player Table
  Create Team Table
  Create base layout(homepage)
  Create platform for new entries
  Create platform to view entries
  Create platform to edit/update entries
  Create platform to delete entries
  Create realtime table
  Add authentication/log in
  Mobile Layout
  Deploy


Draft Information:
  Team Name
  Player Name

Ideal User Layout:
  Team Name   Player Name(drafted)   Round Drafted

#How the project went
The project started off smoothly with the Pusher tutorial and then on to implementing my own draft idea to it.
I ran into some issues with getting the login to work and decided to wait on getting the login since it isn't terribly important for my project(getting my players and teams working came first).
Styling was overall the best part of this project. I found some colors that fit the Turkeybowl vibe and rolled with them.
The login came back to haunt me because two days before this was due, my project broke while I was trying to implement the login.
Having it break at the end of class on Monday only gave me Tuesday to scrap together a working project and get it up on Heroku.
As of writing this, it is technically up on Heroku but the routes don't fully work.
If I had more time I would finish implementing what I had before the last instance of my project broke.
I had a working API, as well as all of my routes built out so getting a login and visualizations was all I needed.

#Workflow
We used Trello and Scrum. We utilized daily stand ups as well as our Trello boards as a means to stay on track and on top of our projects. We were able to set realistic Sprint goals using Trello and it helped me visualize when I fell behind or if I was moving faster than expected.

#Sprint Goals
I had goals depending on where I was with the project.
Building the tutorial was my first Sprint goal and after that came implementing a base layout and the ability to "draft" players. My last sprint goal was to have this deployed with everything, however I did not get to utilize visualizations or the API I had built.

#Security
Overall I think this project is relatively secure. There isn't that is capable of being broken(stolen information, etc).
There are a few security risks in having certain keys in my code on Github but I did not have the time to set them with environment variables.

#Tools
I started with this Pusher tutorial https://pusher.com/tutorials/live-table-flask.
Flask was pretty handy in having a lot of things that I needed without having to download or install too many other packages.
Heroku required packages such as gunicorn, psycopg2, etc.
After my project broke I used https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world as a baseline to start my project with the proper file format. This provided many perks such as having a working login example and even a section on deploying to Heroku.

#Dream scenario aka if I had more time
If I had more time I would definitely find some way to utilize some kind of visualization and an API.
I wanted to style my project a little differently as well.
