# Bonneville Power Administration Capstone Project
## Fa/Wi '14-'15 - Portland State University, Team C

### License Infromation
This project is protected by the GPL 2.0 license. For full license information, see LICENSE file.

### Overview
Our goal in this Capstone project is to create a front-end web interface for the Bonneville Power Administration (BPA). This interface allows users to easily create and send queries to the BPA's database. Some features include a status meter, savable queries, and a dashboard so that users are able to submit multiple queries at once and monitor the jobs' status.

### Background
The BPA is currently collecting 20 TB of data a month, stored as flat files and recorded 1 minute apart. Since there is a single researcher who queries the database using hacked MatLab, and since the database is large and unwieldy, a query may take up to 3 days to complete. In order to help speed up the process, our interface allows other researchers to easily query the database without the need to learn and hack MatLab.

### Assumptions
The following assumptions were made
* The query engine back end is not complete
* The technical background and knowledge of our users varies
* The project runs on its own server
* Use of JSON objects in the query engine
* Firefox and Internet Explorer are the primary supported web browsers

### Features
Features of this project include
* Login page:
  * Multiple users are able to log into their own dashboard
* Dashboard page:
  * Check the status of recent queries 
  * See a summary of query results in graphs
  * Select a single query from the history and view the results
  * Check how much space is left in a node (extra)
* Query creation page:
  * Drop down boxes and text boxes to assist in building queries
  * Ability to specify time range, stations, signal names, conditions
  * User can upload an analysis file to send with query
* Query results page:
  * Results from a single query
  * Time it took to run

### Contributors
Project Manager: Garrison Jensen

User Needs Analyst: Shu Ping Chu

Point of Contact: Matei Mitaru

QA & Testing: Eric Olson

Development Operations: Dan Wilson

Development & Design: Brady St. John, Dan Wilson, Eric Olson, Garrison Jensen, Matei Mitaru, Shu Ping Chu, Zaynab Alattar

Documentation: Zaynab Alattar