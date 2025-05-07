# -*- coding: utf-8 -*-
"""
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
Have a good summer!
"""

from flask import Flask, request, jsonify
import sqlite3
import logging
import random



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

logger = logging.getLogger(__name__)
logging.basicConfig(filename= 'teambattle.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

db = "teambattle.db"

#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#
 #
  # POKEMON
 #
#
@app.route("/pokemon", methods=['GET','POST'])
def pokemon():
    data = request.get_json()

##    

    if not data:
        logging.error('Invalid or Missing JSON when attempting Pokemon.')
        return jsonify({
            "Error": "Invalid or missing JSON",
            "Message": "Request must contain valid JSON",
        }), 400
    
    
    
    
#   
 #POKEMON GET
#
    if request.method == 'GET':
        
        
        pokemonID = data.get('ID')
        pokemonName = data.get('Name')
        
        
    #Error -- Poke Name & ID Used
    
        if pokemonID and pokemonName:
            logging.error('Error: Cannot search Pokemon using both Name and ID')
            return jsonify({
                "Error": "Cannot search Pokemon using both Name and ID",
                "Message": "Request must use either name OR ID",
            }), 400
        
    #If Pokemon ID Used...
    
        if pokemonID:
            try:
                pokemonID = int(pokemonID)
            except ValueError:
                logging.error('Error: Pokemon ID entered not an integer.')
                return jsonify({
                    "Error": "Invalid Pokemon ID",
                    "Message": "Pokemon ID must be an integer",
                }), 400
            
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT * FROM POKEMON WHERE ID = ?", (pokemonID,))
                pokemon = c.fetchone()
                conn.commit
                conn.close()
                
         #No Pokemon found...       
                if pokemon is None:
                    logging.error(f"Pokemon with ID {pokemonID} not found.")
                    return jsonify({
                        "Error": "Pokemon not found.",
                        "Message": f"Pokemon with ID {pokemonID} not found.",
                    }), 400
                
                logging.debug(f"Pokemon with ID {pokemonID} found.")
                return jsonify(
                    {"Message" : "Pokemon found.",
                     "POKEMON" : {
                            "ID": pokemon['ID'],
                            "Name": pokemon['Name'],
                            "Height": pokemon['Height'],
                            "Weight": pokemon['Weight'],
                            "Experience": pokemon['Experience']}
                                }), 200
            except Exception as e:
                logging.error("Database error: {e}")
                return jsonify({"Error" : e}), 400
    
        #If Pokemon Name Used...    
            
        elif pokemonName:
            
                pokemonName = pokemonName.lower()
                
                try:
                   conn = sqlite3.connect(db)
                   conn.row_factory = sqlite3.Row
                   c = conn.cursor()
                   c.execute("SELECT * FROM POKEMON WHERE NAME = ?", (pokemonName,))
                   pokemon = c.fetchone()
                   conn.commit
                   conn.close()
                   
            #No Pokemon found...       
                   if pokemon is None:
                       logging.error(f"Pokemon with name '{pokemonName}' not found.")
                       return jsonify({
                           "Error": "Pokemon not found.",
                           "Message": f"Pokemon with name '{pokemonName}' not found.",
                           }), 400
                   
                   logging.debug(f"Pokemon with name '{pokemonName}' found.")
                   return jsonify(
                       {"Message" : f"Pokemon '{pokemonName}' found.",
                        "POKEMON" : {
                                   "ID": pokemon['ID'],
                                   "Name": pokemon['Name'],
                                   "Height": pokemon['Height'],
                                   "Weight": pokemon['Weight'],
                                   "Experience": pokemon['Experience']}
                               }),200
                except Exception as e:
                    logging.error(f"Database error: {e}")
                    return jsonify({"Error" : e}), 400
                
        ##
        return jsonify({
            "Error": "Unhandled request",
            "Message": "Ensure your request is using either ID or Name with a valid method"
                }), 400
    
    
    
    
    
    
    
#
 #POKEMON POST
# 
    if request.method == 'POST':
        data = request.get_json()
        
    #Set required fields
        requiredData = ['ID', 'Name', 'Height', 'Weight', 'Experience']
        
        for field in requiredData:
            if not data.get(field):
                logging.error(f"{(field).upper()} field missing.")
                return jsonify({ "Error" : "Missing field",
                                "Message" : f"{field} is required"}), 400
        
        
       
        ID = data.get("ID")
        Name = data.get('Name')
        Height = data.get('Height')
        Weight = data.get('Weight')
        Experience = data.get('Experience')
        
     
        
     
        try:
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
        #Duplicate check
            c.execute("SELECT 1 FROM POKEMON WHERE ID = ?", (ID,))
            if c.fetchone():
                logging.error(f"Duplicate ID attempted: {ID}")
                return jsonify({
                    "Error" : "Duplicate ID",
                    "Message" : f"A pokemon with ID {ID} already exists."
                    }), 400
            
        #If no duplicate add POkeon
            q = "INSERT INTO POKEMON(ID,Name,Height,Weight,Experience) VALUES(?,?,?,?,?)"
            c.execute(q, (ID, Name, Height, Weight, Experience))
            
            conn.commit()
            conn.close()
            
            logging.debug(f"Pokemon with ID {ID} added sucessfully.")
            return jsonify(
                {"Message" : f"Pokemon with ID {ID} added successfully.",
                 "POKEMON" : {
                            "ID": ID,
                            "Name": Name,
                            "Height": Height,
                            "Weight": Weight,
                            "Experience": Experience}
                        }),200
        except Exception as e:
            logging.error(f"Database error: {e}")
            return jsonify({"Error" : str(e)}), 400













#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#
  #
   # TRAINER
  #
#



@app.route("/trainer", methods=['GET','POST', 'DELETE'])
def trainer():
    data = request.get_json()


    if not data:
        logging.error('Invalid or Missing JSON when attempting Trainer.')
        return jsonify({
            "Error": "Invalid or missing JSON",
            "Message": "Request must contain valid JSON",
        }), 400
    
    
    
#   
 #TRAINER GET
#
    if request.method == 'GET':
        
        
        trainerID = data.get('ID')
        trainerName = data.get('Name')
        
        
    #Error -- Trainer Name & ID Used
    
        if trainerID and trainerName:
            logging.error('Error: Cannot search Trainer using both Name and ID')
            return jsonify({
                "Error": "Invalid JSON",
                "Message": "Request must use either name OR ID",
            }), 400
        
    #If Trainer ID Used...
    
        if trainerID:
            try:
                trainerID = int(trainerID)
            except ValueError:
                logging.error('Error: Trainer ID entered not an integer.')
                return jsonify({
                    "Error": "Invalid Trainer ID",
                    "Message": "Trainer ID must be an integer",
                }), 400
            
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT * FROM Trainer WHERE ID = ?", (trainerID,))
                trainer = c.fetchone()
                conn.commit
                conn.close()
                
         #No Trainer found...       
                if trainer is None:
                    logging.error(f"Trainer with ID {trainerID} not found.")
                    return jsonify({
                        "Error": "Trainer not found.",
                        "Message": f"Trainer with ID {trainerID} not found.",
                    }), 400
                
                logging.debug(f"Trainer with ID {trainerID} found.")
                return jsonify(
                    {"Message" : f"Trainer with ID {trainerID} found.",
                     "TRAINER" : {
                            "ID": trainer['ID'],
                            "Name": trainer['Name'],
                            "Email": trainer['Email'],
                            "Phone": trainer['Phone'],
                            "Team": trainer['Team']}
                                }), 200
            
            
            except Exception as e:
                logging.error("Database error: {e}")
                return jsonify({"Error" : e}), 400
    
    #If Trainer Name Used...    
            
        elif trainerName:
                
                try:
                   conn = sqlite3.connect(db)
                   conn.row_factory = sqlite3.Row
                   c = conn.cursor()
                   c.execute("SELECT * FROM TRAINER WHERE LOWER(Name) = LOWER(?)", (trainerName,))
                   trainer = c.fetchone()
                   conn.commit
                   conn.close()
                   
            #No Trainer found...       
                   if trainer is None:
                       logging.error(f"Trainer with name '{trainerName}' not found.")
                       return jsonify({
                           "Error": "Trainer not found.",
                           "Message": f"Trainer with name '{trainerName}' not found.",
                           }), 400
                   
                   logging.debug(f"Trainer with name '{trainerName}' found.")
                   return jsonify(
                       {"Message" : f"Trainer '{trainerName}' found.",
                        "TRAINER" : {
                                   "ID": trainer['ID'],
                                   "Name": trainer['Name'],
                                   "Email": trainer['Email'],
                                   "Phone": trainer['Phone'],
                                   "Team": trainer['Team']}
                               }),200
                except Exception as e:
                    logging.error(f"Database error: {e}")
                    return jsonify({"Error" : e}), 400
                
        ##
        return jsonify({
            "Error": "Unhandled request",
            "Message": "Ensure your request is using either ID or Name with a valid method"
                }), 400
    
    
    
    
    
#
 #TRAINER POST
#  
    if request.method == 'POST':
        data = request.get_json()
        requiredData = ['Name', 'Email', 'Phone']
        data['Team'] = data.get('Team', None)
        
        
        
        for field in requiredData:
            if not data.get(field):
                logging.error(f"{(field).upper()} field missing.")
                return jsonify({ "Error" : "Missing field",
                                "Message" : f"{field} is required"}), 400
        
        
       
        Name = data.get('Name').title()
        Email = data.get('Email')
        Phone = data.get('Phone')
        Team = data.get('Team')
        
        
        
        try:
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
        #Duplicate check/assign random id
            while True:
                ID = random.randint(000,999)
                c.execute("SELECT 1 FROM TRAINER WHERE ID =?", (ID,))
                if not c.fetchone():
                    break
            
        #If no duplicate
            
            q = "INSERT INTO TRAINER(ID,Name,Email,Phone,Team) VALUES(?,?,?,?,?)"
            c.execute(q, (ID, Name, Email, Phone, Team))
            
            conn.commit()
            conn.close()
            
            logging.debug(f"Trainer {Name} added sucessfully.")
            return jsonify(
                {"Message" : f"Trainer {Name} added successfully.",
                 "TRAINER" : {
                            "ID": ID,
                            "Name": Name,
                            "Email": Email,
                            "Phone": Phone,
                            "Team": Team}
                        }),200
        except Exception as e:
            logging.error(f"Database error: {e}")
            return jsonify({"Error" : str(e)}), 400
        
            
        
#   
 #TRAINER DEL
#

    if request.method == 'DELETE':
        
        
        trainerID = data.get('ID')
        trainerName = data.get('Name')
        
        
    #Error -- Trainer Name & ID Used
    
        if trainerID and trainerName:
            logging.error('Error: Cannot delete Trainer using both Name and ID')
            return jsonify({
                "Error": "Invalid JSON",
                "Message": "Request must use either name OR ID",
            }), 400
        
    #If Trainer ID Used...
    
        if trainerID:
            try:
                trainerID = int(trainerID)
            except ValueError:
                logging.error('Error: Trainer ID entered not an integer.')
                return jsonify({
                    "Error": "Invalid Trainer ID",
                    "Message": "Trainer ID must be an integer",
                }), 400
            
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                
         #What trainer am I deleting...
                c.execute("SELECT * FROM TRAINER WHERE ID = ?", (trainerID,))
                trainer = c.fetchone()
                
         #No Trainer found...       
                if trainer is None:
                    logging.error(f"Trainer with ID {trainerID} not found.")
                    return jsonify({
                        "Error": "Trainer not found.",
                        "Message": f"Trainer with ID {trainerID} not found.",
                    }), 400
                
                
         #Now delete
         
                c.execute("DELETE FROM TRAINER WHERE ID = ?", (trainerID,))
                conn.commit()
                conn.close()
                logging.debug(f"Trainer with ID {trainerID} sucessfully deleted.")
                return jsonify(
                    {"Message" : "Trainer deleted.",
                     "TRAINER DELETED" : {
                            "ID": trainer['ID'],
                            "Name": trainer['Name'],
                            "Email": trainer['Email'],
                            "Phone": trainer['Phone'],
                            "Team": trainer['Team']}
                                }), 200
            except Exception as e:
                logging.error("Database error: {e}")
                return jsonify({"Error" : e}), 400
    
    #If Trainer Name Used...    
            
        elif trainerName:
            
                trainerName = trainerName.lower()
                
                try:
                   conn = sqlite3.connect(db)
                   conn.row_factory = sqlite3.Row
                   c = conn.cursor()
                   
                   #What trainer am I deleting
                   c.execute("SELECT * FROM TRAINER WHERE LOWER(Name) = LOWER(?)", (trainerName,))
                   trainer = c.fetchone()
                   
                   
            #No Trainer found...       
                   if trainer is None:
                       logging.error(f"Trainer with name '{trainerName}' not found.")
                       return jsonify({
                           "Error": "Trainer not found.",
                           "Message": f"Trainer with name '{trainerName}' not found.",
                           }), 400
                   
            #Delete        
                    
                   c.execute("DELETE FROM TRAINER WHERE LOWER(Name) = LOWER(?)", (trainerName,))
                   conn.commit()
                   conn.close()
                   
                   
                   logging.debug(f"Trainer with name '{trainerName}' deleted.")
                   return jsonify(
                       {"Message" : f"Trainer '{trainerName}' deleted.",
                        "TRAINER DELETED" : {
                                   "ID": trainer['ID'],
                                   "Name": trainer['Name'],
                                   "Email": trainer['Email'],
                                   "Phone": trainer['Phone'],
                                   "Team": trainer['Team']}
                               }),200
                except Exception as e:
                    logging.error(f"Database error: {e}")
                    return jsonify({"Error" : e}), 400
                
        logging.error("Error: Unhandled request.")
        return jsonify({
            "Error": "Unhandled request",
            "Message": "Ensure your request is using either ID or Name with a valid method"
                }), 400
        
        

#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#
  #
   # TEAM
  #
#
@app.route("/team", methods=['GET','POST', 'DELETE'])
def team():
    data = request.get_json()


    if not data:
        logging.error('Invalid or Missing JSON when attempting Team.')
        return jsonify({
            "Error": "Invalid or missing JSON",
            "Message": "Request must contain valid JSON",
        }), 400


#
 #Team POST
# 
    if request.method == 'POST':
        data = request.get_json()
        
        
        Name = data.get('Name')
        Manager = data.get('Manager')
        ManagerName = data.get('ManagerName')
        
        
        if not Manager and not ManagerName:
            return jsonify({
                "Error": "Missing required trainer information: Manager.",
                "Message": "You must provide either 'Manager' (Trainer's ID) or 'ManagerName'."
                }), 400
       
        if not Name:
            return jsonify({
                "Error": "Missing required trainer information: Name.",
                "Message": "You must provide team Name."
                }), 400
        
        
        
        
        try:
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
        #If user wants to use trainer name not id   
            if ManagerName and not Manager:
                c.execute("SELECT ID FROM TRAINER WHERE Name = ?", (ManagerName.title(),))
                trainer = c.fetchone()
                if not trainer:
                    return jsonify({
                        "Error": f"No trainer found with name '{ManagerName}'",
                        "Message": "Please create this trainer before assigning them to a team."
                        }), 400
                Manager = trainer["ID"]
            
            
        #Assign team ID
            while True:
                ID = random.randint(000,999)
                c.execute("SELECT 1 FROM TEAM WHERE ID =?", (ID,))
                if not c.fetchone():
                    break
                
#######           
        #Make sure Manager exists
            c.execute("SELECT * FROM TRAINER WHERE ID = ?", (Manager,))
            trainer = c.fetchone()
            if not trainer:
                return jsonify({
                    "Error": f"No trainer found with ID {Manager}",
                    "Message": "Please create the trainer before assigning them as a team manager.",
                    "Message2": "If you do not know your trainer's ID, you may use their name as ManagerName."
                    }), 400
            
        #If no duplicate
            
            q = "INSERT INTO TEAM(ID,Name,Manager) VALUES(?,?,?)"
            c.execute(q, (ID, Name, Manager))
            c.execute("SELECT * FROM TEAM WHERE ID = ?", (ID,))
            Team = c.fetchone()
            
            #Does trainer exist? If yes update their Trainer "Team" Field
            
            c.execute("SELECT * FROM TRAINER WHERE ID = ?", (Manager,))
            Trainer = c.fetchone()
            
            if not ManagerName:
                ManagerName = Trainer['Name']
            
            
            
            if Trainer:
                c.execute("UPDATE TRAINER SET Team = ? Where ID = ?", (ID, Trainer["ID"]))
            conn.commit()
            conn.close()
            
            logging.debug(f"Team {Name} added sucessfully.")
            return jsonify(
                {"Message" : f"Team {Name} added successfully.",
                 "Team" : {
                            "ID": Team['ID'],
                            "Name": Team['Name'],
                            "Manager": Team['Manager'],
                            "ManagerName" : ManagerName,
                            "Wins": Team['Wins'],
                            "Losses": Team['Losses']}
                        }),200
        except Exception as e:
            logging.error(f"Database error: {e}")
            return jsonify({"Error" : str(e)}), 400
        
#   
 #TEAM GET
#
    if request.method == 'GET':
        
        
        teamID = data.get('ID')
        teamName = data.get('Name')
        
        
    #Error -- Team Name & ID Used
    
        if teamID and teamName:
            logging.error('Error: Cannot search Team using both Name and ID')
            return jsonify({
                "Error": "Invalid JSON",
                "Message": "Request must use either name OR ID",
            }), 400
        
    #If Team ID Used...
    
        if teamID:
            try:
                teamID = int(teamID)
            except ValueError:
                logging.error('Error: Team ID entered not an integer.')
                return jsonify({
                    "Error": "Invalid Team ID",
                    "Message": "Team ID must be an integer",
                }), 400
            
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT * FROM Team WHERE ID = ?", (teamID,))
                team = c.fetchone()
                conn.close()
                
         #No Team found...       
                if team is None:
                    logging.error(f"Team with ID {teamID} not found.")
                    return jsonify({
                        "Error": "Team not found.",
                        "Message": f"Team with ID {teamID} not found.",
                    }), 400
                
                logging.debug(f"Team with ID {teamID} found.")
                return jsonify(
                    {"Message" : f"Team with ID {teamID} found.",
                     "TEAM" : {
                            "ID": team['ID'],
                            "Name": team['Name'],
                            "Manager": team['Manager'],
                            "Wins": team['Wins'],
                            "Losses": team['Losses']}
                                }), 200
            
            
            except Exception as e:
                logging.error("Database error: {e}")
                return jsonify({"Error" : e}), 400
    
    #If Team Name Used...    
            
        elif teamName:
                
                try:
                   conn = sqlite3.connect(db)
                   conn.row_factory = sqlite3.Row
                   c = conn.cursor()
                   c.execute("SELECT * FROM TEAM WHERE LOWER(Name) = LOWER(?)", (teamName,))
                   team = c.fetchone()
                   conn.close()
                   
            #No Team found...       
                   if team is None:
                       logging.error(f"Team with name '{teamName}' not found.")
                       return jsonify({
                           "Error": "Team not found.",
                           "Message": f"Team with name '{teamName}' not found.",
                           }), 400
                   
                   logging.debug(f"Team with name '{teamName}' found.")
                   return jsonify(
                       {"Message" : f"Team with name {teamName} found.",
                        "TEAM" : {
                               "ID": team['ID'],
                               "Name": team['Name'],
                               "Manager": team['Manager'],
                               "Wins": team['Wins'],
                               "Losses": team['Losses']}
                                   }), 200
                except Exception as e:
                    logging.error(f"Database error: {e}")
                    return jsonify({"Error" : e}), 400
                
        ##
        return jsonify({
            "Error": "Unhandled request",
            "Message": "Ensure your request is using either ID or Name with a valid method"
                }), 400
    





#   
 #TEAM DEL
#

    if request.method == 'DELETE':
        
        
        teamID = data.get('ID')
        teamName = data.get('Name')
        
        
    #Error -- Team Name & ID Used
    
        if teamID and teamName:
            logging.error('Error: Cannot delete Team using both Name and ID')
            return jsonify({
                "Error": "Invalid JSON",
                "Message": "Request must use either name OR ID",
            }), 400
        
    #If Team ID Used...
    
        if teamID:
            try:
                teamID = int(teamID)
            except ValueError:
                logging.error('Error: Team ID entered not an integer.')
                return jsonify({
                    "Error": "Invalid Team ID",
                    "Message": "Team ID must be an integer",
                }), 400
            
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                
         #What team am I deleting...
                c.execute("SELECT * FROM TEAM WHERE ID = ?", (teamID,))
                team = c.fetchone()
                
         #No Team found...       
                if team is None:
                    logging.error(f"Team with ID {teamID} not found.")
                    return jsonify({
                        "Error": "Team not found.",
                        "Message": f"Team with ID {teamID} not found.",
                    }), 400
                
                
         #Now delete
         
                c.execute("DELETE FROM TEAM WHERE ID = ?", (teamID,))
                conn.commit()
                conn.close()
                logging.debug(f"Team with ID {teamID} sucessfully deleted.")
                return jsonify(
                    {"Message" : f"Team with ID {team['ID']} deleted.",
                     "DELETING TEAM" : {
                            "ID": team['ID'],
                            "Name": team['Name'],
                            "Manager": team['Manager'],
                            "Wins": team['Wins'],
                            "Losses": team['Losses']}
                                }), 200
            except Exception as e:
                logging.error("Database error: {e}")
                return jsonify({"Error" : e}), 400
    
    #If Team Name Used...    
            
        elif teamName:
            
                teamName = teamName.lower()
                
                try:
                   conn = sqlite3.connect(db)
                   conn.row_factory = sqlite3.Row
                   c = conn.cursor()
                   
                   #What team am I deleting
                   c.execute("SELECT * FROM TEAM WHERE LOWER(Name) = LOWER(?)", (teamName,))
                   team = c.fetchone()
                   
                   
            #No Team found...       
                   if team is None:
                       logging.error(f"Team with name '{teamName}' not found.")
                       return jsonify({
                           "Error": "Team not found.",
                           "Message": f"Team with name '{teamName}' not found.",
                           }), 400
                   
            #Delete        
                   c.execute("UPDATE TRAINER SET Team = NULL WHERE Team = ?", (team["ID"],)) 
                   c.execute("DELETE FROM TEAM WHERE LOWER(Name) = LOWER(?)", (teamName,))
                   conn.commit()
                   conn.close()
                   
                   
                   logging.debug(f"Team with name '{teamName}' deleted.")
                   return jsonify(
                       {"Message" : f"Team with Name {team['Name']} deleted.",
                        "DELETING TEAM" : {
                               "ID": team['ID'],
                               "Name": team['Name'],
                               "Manager": team['Manager'],
                               "Wins": team['Wins'],
                               "Losses": team['Losses']}
                                   }), 200
                except Exception as e:
                    logging.error(f"Database error: {e}")
                    return jsonify({"Error" : e}), 400
                
        logging.error("Error: Unhandled request.")
        return jsonify({
            "Error": "Unhandled request",
            "Message": "Ensure your request is using either ID or Name with a valid method"
                }), 400
                
      
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#
  #
   # MEMBERSHIP
  #
#
@app.route("/membership", methods=['POST', 'DELETE'])
def membership():
    data = request.get_json()


    if not data:
        logging.error('Invalid or Missing JSON when attempting to GET Team.')
        return jsonify({
            "Error": "Invalid or missing JSON",
            "Message": "Request must contain valid JSON",
        }), 400
    
    
#
 #MEMBERSHIP POST
# 

    if request.method == 'POST':
        data = request.get_json()
        
        TeamID = data.get("TeamID")
        TeamName = data.get("TeamName")
        if TeamName:
            TeamName = TeamName.lower()
        PokemonID = data.get("PokemonID")
        PokemonName = data.get("PokemonName")
        if PokemonName:
            PokemonName = PokemonName.lower()
        
        
        
        
    #Make sure one of each field for Pokemon & Team are put in... doesn't have to be both. 


        
        if not (PokemonID or PokemonName):
           logging.error("Missing Pokemon identifier")
           return jsonify({"Error": "Must provide either PokemonID or PokemonName"}), 400

        if not (TeamID or TeamName):
            logging.error("Missing team identifier")
            return jsonify({"Error": "Must provide either TeamID or TeamName"}), 400
     
        
        try:
            
            
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
   ##Account for input of Team/Pokemon Name OR ID



            
   #User entered TeamName and not Team ID?
            if TeamName and not TeamID:
                c.execute("SELECT ID FROM Team WHERE LOWER(Name) = LOWER(?)", (TeamName,))
                TeamRow = c.fetchone()
                
                
                
    #First does the team exist
                if not TeamRow:
                    logging.error(f"Team '{TeamName}' does not exist.")
                    return jsonify({"Error": f"Team '{TeamName}' does not exist"}), 400
               
                
               
    #Then Set team ID based off of team name
                TeamID = TeamRow["ID"]
                
                
                
                
    #OR, if they just enter the Team ID
    #Validate Team ID Input
            elif TeamID:
                try:
                    TeamID = int(TeamID)
                except ValueError:
                    logging.error("Team ID entered is not an integer")
                    return jsonify({"Error": "Team ID must be an integer"}), 400
   
    
   #If they don't enter either...
            else:
                logging.error("Must provide either TeamID or TeamName")
                return jsonify({"Error": "Must provide either TeamID or TeamName"}), 400
            
 #######################################           
    #User enteres POkemon Name but not Id...
            if PokemonName and not PokemonID:
                c.execute("SELECT ID FROM Pokemon WHERE LOWER(Name) = LOWER(?)", (PokemonName,))
                PokemonRow = c.fetchone()
    
    
    #Does POkemon Exist?            
                if not PokemonRow:
                    logging.error(f"Pokemon '{PokemonName}' not found.")
                    return jsonify({"Error": f"Pokemon '{PokemonName}' not found"}), 400
    
        
    
    #Set Pokemon ID from Name
                PokemonID = PokemonRow["ID"]
                
    #OR ID entered, validate it, & what if they don't enter either...
            elif PokemonID:
                try:
                    PokemonID = int(PokemonID)
                except ValueError:
                    logging.error("Pokemon ID must be an integer")
                    return jsonify({"Error": "Pokemon ID must be an integer"}), 400
            else:
                logging.error("Must provide either PokemonID or PokemonName")
                return jsonify({"Error": "Must provide either PokemonID or PokemonName"}), 400
             
 
    
    ##Check Team parameters 
    
 
        # Check Duplicate
            
            c.execute("SELECT 1 FROM MEMBERSHIP WHERE TeamID = ? AND PokemonID = ?", (TeamID, PokemonID))
            if c.fetchone():
                logging.error("Error: Can't assign duplicate Pokemon to team.")
                return jsonify({
                    "Error": "Duplicate entry",
                    "Message": f"Pokemon {PokemonID} is already on Team {TeamID}."
                }), 400
            
            
        # Check for 6 Teammembers
            
            c.execute("SELECT COUNT(*) as count FROM MEMBERSHIP WHERE TeamID = ?", (TeamID,))
            count = c.fetchone()["count"]
            if count >= 6:
                logging.error(f"Team {TeamID} already has 6 members.")
                return jsonify({
                "Error": "Team full",
                "Message": f"Team {TeamID} already has 6 members."
            }), 400
            
            
        #Now you can add membership
            
            c.execute("INSERT INTO MEMBERSHIP (TeamID, PokemonID) VALUES (?, ?)", (TeamID, PokemonID))
          
            
            
#Temporarily see TeamID name and PokemonID Name, but don't append them to table...
#Cause we just want everything to run off of ID #s
#Also want this to work if user just had ID # but no names. Basically names optional but functional


    

            c.execute("""
                      SELECT 
                      TEAM.Name AS TeamName,
                      POKEMON.Name AS PokemonName
                      FROM MEMBERSHIP
                      JOIN TEAM ON MEMBERSHIP.TeamID = TEAM.ID
                      JOIN POKEMON ON MEMBERSHIP.PokemonID = POKEMON.ID
                      WHERE MEMBERSHIP.TeamID = ? AND MEMBERSHIP.PokemonID = ?
                      """, (TeamID, PokemonID))
        
            row = c.fetchone()
            conn.commit()
            conn.close()
    
            logging.debug(f"Pokemon {PokemonID} added to team {TeamID} successfully")
            return jsonify(
                {"Message" : f"Pokemon {PokemonID} added to team {TeamID} successfully",
                 "Member" : {
                           "TeamID": TeamID,
                           "Team_Name" : row['TeamName'],
                           "PokemonID": PokemonID,
                           "Pokemon_Name" : row['PokemonName']
                       }}),200
        except Exception as e:
            logging.error(f"Database error: {e}")
            return jsonify({"Error" : str(e)}), 400
        
        
        
        
#
 #MEMBERSHIP DELETE
#


#Basically copy post data but make it delete...


    if request.method == 'DELETE':
        data = request.get_json()
        
        TeamID = data.get("TeamID")
        TeamName = data.get("TeamName")
        if TeamName:
            TeamName = TeamName.lower()
        PokemonID = data.get("PokemonID")
        PokemonName = data.get("PokemonName")
        if PokemonName:
            PokemonName = PokemonName.lower()
        
        
        
        
        #Make sure one of each field for Pokemon & Team are put in... doesn't have to be both. 


        
        if not (PokemonID or PokemonName):
           logging.error("Missing Pokemon identifier")
           return jsonify({"Error": "Must provide either PokemonID or PokemonName"}), 400

        if not (TeamID or TeamName):
            logging.error("Missing team identifier")
            return jsonify({"Error": "Must provide either TeamID or TeamName"}), 400
            
    

        
        
        try:
            
            
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
    ##Account for input of Team/Pokemon Name OR ID



            
   #User entered TeamName and not Team ID?
            if TeamName and not TeamID:
                c.execute("SELECT ID FROM TEAM WHERE LOWER(Name) = LOWER(?)", (TeamName,))
                Team = c.fetchone()
                
                
                
    #First does the team exist
                if not Team:
                    logging.error(f"Team '{TeamName}' does not exist.")
                    return jsonify({"Error": f"Team '{TeamName}' does not exist"}), 400
               
                
               
    #Then Set team ID based off of team name
                TeamID = Team["ID"]
                
                
                
                
    #OR, if they just enter the Team ID
    #Validate Team ID Input
            elif TeamID:
                try:
                    TeamID = int(TeamID)
                except ValueError:
                    logging.error("Team ID entered is not an integer")
                    return jsonify({"Error": "Team ID must be an integer"}), 400
   
    
   #If they don't enter either...
            else:
                logging.error("Must provide either TeamID or TeamName")
                return jsonify({"Error": "Must provide either TeamID or TeamName"}), 400
            
            
    #User enteres POkemon Name but not Id...
            if PokemonName and not PokemonID:
                c.execute("SELECT ID FROM POKEMON WHERE LOWER(Name) = LOWER(?)", (PokemonName,))
                Pokemon = c.fetchone()
    
    
    #Does POkemon Exist?            
                if not Pokemon:
                    logging.error(f"Pokemon '{PokemonName}' not found.")
                    return jsonify({"Error": f"Pokemon '{PokemonName}' not found"}), 400
    
        
    
    #Set Pokemon ID from Name
                PokemonID = Pokemon["ID"]
                
    #OR ID entered, validate it, & what if they don't enter either...
            elif PokemonID:
                try:
                    PokemonID = int(PokemonID)
                except ValueError:
                    logging.error("Pokemon ID must be an integer")
                    return jsonify({"Error": "Pokemon ID must be an integer"}), 400
            else:
                logging.error("Must provide either PokemonID or PokemonName")
                return jsonify({"Error": "Must provide either PokemonID or PokemonName"}), 400
             
 
    
   
            
            c.execute("SELECT * FROM MEMBERSHIP WHERE TeamID = ? AND PokemonID = ?", (TeamID, PokemonID))
            c.execute("""
                      SELECT 
                      TEAM.Name AS TeamName,
                      POKEMON.Name AS PokemonName
                      FROM MEMBERSHIP
                      JOIN TEAM ON MEMBERSHIP.TeamID = TEAM.ID
                      JOIN POKEMON ON MEMBERSHIP.PokemonID = POKEMON.ID
                      WHERE MEMBERSHIP.TeamID = ? AND MEMBERSHIP.PokemonID = ?
                      """, (TeamID, PokemonID))
            pokemon = c.fetchone()
            
     #Does this pokemon even go here?
            if not pokemon:
                logging.error(f"Pokemon ID {PokemonID} is not a member of Team ID {TeamID}")
                return jsonify({"Error": "Membership not found"}), 400
       #delete 
            c.execute("DELETE FROM MEMBERSHIP WHERE TeamID = ? AND PokemonID = ?", (TeamID, PokemonID))            
            conn.commit()
            conn.close()
    
            logging.debug(f"Pokemon {PokemonID} deleted from team {TeamID} successfully")
            return jsonify(
                {"Message" : f"Pokemon {PokemonID} deleted from team {TeamID}",
                 "MEMBER DELETED" : {
                           "TeamID": TeamID,
                           "Team_Name" : pokemon['TeamName'],
                           "PokemonID": PokemonID,
                           "Pokemon_Name" : pokemon['PokemonName']
                       }}),200
        except Exception as e:
            logging.error(f"Database error: {e}")
            return jsonify({"Error" : str(e)}), 400




#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#
  #
   # RANKING
  #
#
@app.route("/ranking", methods=['GET'])
def rankig():
    
 try:
     
     
     conn = sqlite3.connect(db)
     conn.row_factory = sqlite3.Row
     c = conn.cursor()
     c.execute("SELECT ID, Wins, Name\
                FROM Team\
                ORDER BY Wins DESC\
                LIMIT 3")
     Leaderboard = c.fetchall()
     logging.debug("Top 3 teams returned")
     
     TeamData = []
     for row in Leaderboard:
         TeamData.append({"TeamID": row["ID"], "TeamName": row["Name"], "Wins": row["Wins"]})
     return jsonify(
         {"Message" : "Top 3 Pokemon Teams",
          "Team Leaderboard" : TeamData
          }),200
 
 
 except Exception as e:
     logging.error(f"Database error: {e}")
     return jsonify({"Error" : str(e)}), 400
 
    
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````` 
#
  #
   # BATTLE
  #
#
@app.route("/battle", methods=['POST'])
def battle():
    
    if request.method == 'POST':
        data = request.get_json()
        
        
        requiredData = ['team1','team2']
        
        for field in requiredData:
            if not data.get(field):
                logging.error(f"{(field).upper()} field missing.")
                return jsonify({ "Error" : "Missing field",
                                "Message" : f"{field} is required"}), 400
               
            
            
            
        team1 = data.get("team1")
        team2 = data.get("team2")

        try:
            team1 = int(team1)
            team2 = int(team2)
        except ValueError:
            logging.error("One or both Team IDs are not integers")
            return jsonify({"Error": "Both team1 and team2 must be integers"}), 400


        try:
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
   #does team 1 exist         
            c.execute("SELECT * FROM Team WHERE ID = ?", (team1,))
            row1 = c.fetchone()
            if not row1:
                logging.debug(f"Team with ID {team1} not found")
                return jsonify({"Error": f"Team with ID {team1} not found"}), 400
            name1 = row1["Name"]
            
            
            
   #does team 2 exist
            c.execute("SELECT * FROM Team WHERE ID = ?", (team2,))
            row2 = c.fetchone()
            if not row2:
                logging.debug(f"Team with ID {team2} not found")
                return jsonify({"Error": f"Team with ID {team2} not found"}), 400
            name2 = row2["Name"]
            
            
            
    #team1 experience total
            c.execute("""
                SELECT SUM(Pokemon.Experience) AS XP
                FROM Membership
                JOIN Pokemon ON Membership.PokemonID = Pokemon.ID
                WHERE Membership.TeamID = ?
            """, (team1,))
            TeamExperience1 = c.fetchone()["XP"]
            if TeamExperience1 is None:
                logging.debug(f"Team {team1} is empty.")
                return jsonify({"Error": f"Team {team1} is empty"}),400
            
            
    #team2 experience total
            c.execute("""
                SELECT SUM(Pokemon.Experience) AS XP
                FROM Membership
                JOIN Pokemon ON Membership.PokemonID = Pokemon.ID
                WHERE Membership.TeamID = ?
            """, (team2,))
            TeamExperience2 = c.fetchone()["XP"]
            if TeamExperience2 is None:
                logging.debug(f"Team {team2} is empty.")
                return jsonify({"Error": f"Team {team2} is empty"}), 400  
            
            
   #Who wins
            if TeamExperience1 > TeamExperience2:
               winner= team1
               loser = team2
               winnerName = name1
               
               
               
            elif TeamExperience2 > TeamExperience1:
               winner = team2
               loser = team1
               winnerName = name2
               
            else:
               winner = None

    #Share win & Loss data
            if winner:
               c.execute("UPDATE Team SET Wins = Wins + 1 WHERE ID = ?", (winner,))
               c.execute("UPDATE Team SET Losses = Losses + 1 WHERE ID = ?", (loser,))

            conn.commit()
            conn.close()
            
            return jsonify({
                "Message": f"Team {winner} won!" if winner else "It's a tie!",
                "Battle Data": {
                    f"Team {team1} - {name1} XP": TeamExperience1,
                    f"Team {team2} - {name2} XP": TeamExperience2,
                    "Winner": f"{winnerName}" if winner else "Tie"
                }
            }), 200 
            
            
            
        except Exception as e:
            logging.error("Database error")
            return jsonify({"Error": str(e)}), 400     
            
             
        
# #
#  #
#   #
#  #
# #

app.run(host='0.0.0.0', port=9999, debug=False)