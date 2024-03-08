# sqlalchemy_challenge
This module analyzes the climate in Honolulu for a vacation

# Part 1: Analyze and Explore the Climate Data
Use Python and SQLAlchemy to do a basic climate analysis and data exploration.
Complete the following steps:
  1. Use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your   climate analysis and data exploration.
  2. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
  3. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
  4. Link Python to the database by creating a SQLAlchemy session.
  5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

# Precipitation Analysis
  1. Find the most recent date in the dataset.
  2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
  3. Select only the "date" and "prcp" values.
  4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
  5. Sort the DataFrame values by "date".
  6. Plot the results by using the DataFrame plot method.
  7. Use Pandas to print the summary statistics for the precipitation data.

# Station Analysis
  1. Design a query to calculate the total number of stations in the dataset.
  2. Design a query to find the most-active stations.
  3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
  4. Design a query to get the previous 12 months of temperature observation (TOBS) data.

# Part 2: Design Your Climate App
Design a Flask API based on the queries that you just developed.

Create a homepage (/)
Then create the following routes:
  /api/v1.0/precipitation
  /api/v1.0/tobs
  /api/v1.0/tobs
  /api/v1.0/<start>
  /api/v1.0/<start>/<end>

# Resources:
  ReadMe instructions pulled from Columbia University Data Analytics Bootcamp.  https://bootcampspot.instructure.com/courses/4737/assignments/68482?module_item_id=1162171
  Climate data from: Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.
