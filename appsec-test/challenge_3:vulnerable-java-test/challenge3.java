//Example case
// This version allows for abuse because it allows for dynamic queries.
String sql_query = "SELECT * FROM users WHERE userid ='"+ username + "'" + " AND password='" + Base64.getEncoder().encodeToString(passwordString.getBytes()) + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
//End of example
//Answer
// this version fixed parameters for the queries which is the secure controlled way of doing this.
PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users WHERE userid=? AND password=?");
stmt.setString(1, userid);
stmt.setString(2, password);
ResultSet rs = stmt.executeQuery();
