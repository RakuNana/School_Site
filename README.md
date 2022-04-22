# School_Site
No mistakes this time

A website I'm making for school. I'm uploading this so others can help me debug it. Currently I'm trying to get it to use a social login.
The one I'm using is social-auth-app-django however, It keeps giving me an error after I get github to auth. "NoneType" object has no attribute to "provider"
I have an idea of what the problem maybe but, I can't seem to fix it.

What I believe is happening is, the user social auth data is being sent somewhere else instead of the user social auth database. The reason I think this is because after github auths my account, and crashes, I can see it grabbed my user name and my email from github correctly. However, The user social auth remains empty.I'm pretty confident that there's a problem with my urlpatterns redirecting data into the damn sun instead of the user socail auths database. Again I've got no idea how to fix this. I've been at it for about two weeks now and made no progress into solving this problem, I'm just about ready to throw in the towel..... or at the very least hang myself with it.

If you want to help me debug it, GREAT! Just a few things to note, ONE. I erased my db.sqlite3 file because it had my info in it, you'll have to create your
own. TWO I deleted my Github keys and secret, so again you'll have to create your own.

If you want to see what the site looks like, as well as see the problem in action, the site is https://rakunana.pythonanywhere.com 
It's bare bones, so don't expect greatness or whatever, I just need a grade :P

Things I've tried:

Social_auth_pipeline, dosen't work

changing the urlspatterns don't work

using django_allauth crashes the site

I've changed my settings dozens of times, Yes the contexts are there, apps are installed, and I have the redirects

I've changed my urlpatterns dozens of times, doesn't seem to make a difference 

I've added code from others that have had the same problem, didn't fix the issue

I've deleted code, more along the lines to see what actually was working and what wasn't

