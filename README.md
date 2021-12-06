
Contributors -- Bryan Yao and Aryan Nagariya


Routes and Pages:

We have 5 main url pages -- the home page, login page, logout page, profile page, 
a page that displays all hastags, and a page for each individual hastag that displays its respective tweets.The above is from how the code is designed. From the user's point of view, they are first directed to the splash page or (welcome page) that directs them to a the log in/sign up page. Once they have logged in, they see four main buttons -- one to tweet, to see all tweets, to see their tweets, and finally a button that shows them all hashtags. While the first three stay on the same page, the hastag button redirects them to a new page. Once there, they see all hashtags in a hyperlink blue form. If they choose to  click on a hashtag, it will redicect them to a new page that displays all the tweets that contian that specfic hashtag.


Submission Requirements: 

Log In and Sign Up page -- Welcome page, and once they hit "tweet about it", they are directed towards the log in/sign up page
Splash page (explanation of product) -- This is the welcome page, we show the user that this is a Twitter clone by showing them the "tweet about it " button. We also made out UX interface similar to Twitter to make it as crystal clear that our product is a twitter clone.
Home page (feed of tweets and hashtags) -- Once a user is logged in, they see the option to enter a text and to tweet it about by hitting the "tweet" button. A user can see all the tweets by clicking the "All Tweets" button. 
Profile page (display of each users tweets) -- A user can see all of his/her tweets by clicking the "My tweets" button.
Hashtag page (display of the tweets that correspond to a hashtag) -- The main hashtag page can be reached by clicking the "Hastags" button under the Home Page. From there, they can see the list of all hashtags used so far. In order to only see tweets that contain a specific hashtag, the user can click the hyperlink blue hashtag respectively from the main hashtags page. 

Like Button -- Each tweet has a "liked button" that the user can hit and our website will let the know user whether they have liked or not liked a tweet. By default, a user likes all of their own tweets but none of other's user tweets!

Read Me -- This file!

Design Considerations :

Profile Page -- Instead of making a whole new page/url for each user's profile, we incorporated this into the home page while making sure we retain the functionality by making the "My tweets button". The main factor for this decision was that we were only displaying the tweets from a particular user, and hence it would make sense to have it be on the same page. This also makes it easier to toggle between one's tweets and all tweets.

HashTag Methods -- Instead of creating a new Class/App for hastags, we made the releveants methods within the tweet class so that we can individually parse through all tweets as soon as they are made. This made it easier, since we did not have to make our design any more complex.

Storing Hastag and the "#" operator in the URL -- Initially, we were parsing tweets and saving them all in an array in a format that included "#" infront of all the tweets. However, we ran into a problem when we were parsing hastags in the URL to create a new page for all the tweets that contain the particular hashtag. The problem was that "#" is not allowed to be the URL, and we had to instead use "%23" instead of "#". However, we could not make this change within the HTML page since we could not use Python in the file. Our solution to this problem was that in the intial array, instead of storing hastags with the "#" operator, we only saved the characters after the "#" operator. This way, we could create a new URL without running into the problem of having a "#" in the URL. However, from a user's point of view, it did not make any differece, since we just added a "#" before displaying hastags in the frontend instead of the backend. 




