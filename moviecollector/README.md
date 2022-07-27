
# Product Requirements Documentation

**Summary**
| Field | Detail |
|-------|--------|
| Project Name | Movie Collectors App |
| Description | A place for people to share Movies! |
| Developers | Hieu Nguyen |
| Live site | [MovieCollectorsApp](https://moviecollectorsapp.herokuapp.com/) |
| Repo | [GitHubLink](https://github.com/Hieu12319/moviecollectorproj) |
|Trello | [TrelloSite](https://trello.com/b/si2ckNqh/movie-collector-app)


## Things I want to improve

- Inhanced user experience
- Search functionality
- Sort functionality
- Notifications
- Movies API


## User Stories

List of stories users should experience when using your application.

- Users can create an account
- Users can sign in to their account
- Users can create a movie 
- Users can see all movies listed
- Users can update movies
- User can delete movies

## Route Tables

- The endpoint: the URL to which the request must be made
- The method: the type of http method the request should be
- The response: what the response should be, a web page, json data, etc.

| Endpoint | Method | Response |
| -------- | ------ | -------- | 
| /movies | GET | Brings up the Feed  | 
| /movies/create | POST | Create a movie 
| /about/ | GET | Shows the About page | 
| /movies/<int:movies_id>/ | GET | Shows the specific movie | 
| movies/<int:pk>/delete/ | DELETE | delete the movie | 
| accounts/signup/ | POST | creates new user and returns to their movie list page| 

### SNIPPETS 
