From Michael 
============
```

Max’s Code Review for Fake Forum
—————————————————————————————————
Thanks for the opportunity to review your code. 

<idea> is simply a suggestion on usability, nothing more.

Let me know if you have any questions on the following review.
——————————————————————————————————

OVERALL >>> 


The forum looks awesome. Good use of colors and shadows. It has this cool effect of cards floating or 3D. Nice use of JS objects. It took me some time to clarify the JS as strategically using JS objects are still new for me. I hope this helps. 


HTML >>>

L1 — missing <!DOCTYPE html> Declaration
L2-7 — missing <title></title> 
L5 — forward slash not needed at the end of the <link> tag
L6 — Could probably get away with moving the jQuery <script> tag to the bottom above the custom JS script.
L10-11 — <idea> Possibly a comment in <main> tag describing that content is placed here by JavaScript to avoid thinking it is an empty element.
L15 — “for” is not an attribute for <input>; other options may be “value” or “name”. Misspelling of the “placeholder” attribute (once fixed the lighter text appears. Forward slash not needed at the end of the <input> tag
L17 — “for” is not an attribute for <textarea>; Misspelling of the “placeholder” attribute (once fixed the lighter text appears. <idea> “cols” may be required as well or using height and width in the CSS. It looks like it works fine though without it as an attribute.
L18 — Forward slash not needed at the end of the <input> tag



CSS >>>

<idea> It would be a Tiffany question but seems to be strategic to use em or % for horizontal (left-right; width; fonts too) styles and px or fixed for vertical (up-down; height) styling.

L48 — Could probably get away with ‘section’
L59 — Could probably get away with ‘form *’
L65 — Could get away with ‘label’
L67 — It looks like with the Google Font options and specifically Ubuntu in this case, a font-weight of 700 is not an option, just 400. 700 would need to be selected as an option (if it is an option) to use font-weights with Google Fonts.


JS >>>

L8 — <insightful> Interesting how ‘.noConflict()’ works
L62 — <insightful> Nice use of the jQuery multiple selector
L91 — error div message remains after it is triggered to include being followed by a successful post. Nice use of effects.
<idea> Success message
```
Max Response
============

All code can be seen in this diff:
https://github.com/PDXDevCampJuly/max-resnick/commit/f761b01660e6d84d4ba8f6bc9bc71d499d7b6255

HTML
----

* Implemented all

CSS
---

* RE: % vs em. I’ve been using em strictly where I think something should grow as the base font size grows, e.g. padding/margin around content stuff and using % when it’s more layouty things. Not sure how “right” that is though.
* L48, 59, 65 - all implemented.
* L67 - I didn’t specify any font weights in the font URL, but I’m def seeing the items “bold” see attached screenshots

JS
--

* L8 I’ve mostly been doing that because I don’t like `$` as variable name.
* L62  just a CSS selector :-_)
* L91 - added L75 to handle this.
* To add a success messaged I decided to refactor the then() of L79. I factored it out to a single forumPostSucess, which is called on success and error in this case because of the CORS issue.
* Success Message was added on L99

Michael Response 2
==================

```
Hey Max, changes look good. A couple notes: I tested the forum again and noticed the error message still remains after a successful post. I tested it again with the python server you sent just to see if that was the case and it still remains. In addition, the <!DOCTYPE html5> does not need the “5”. We can talk more tomorrow and see it running on your computer. Thanks for taking the changes into consideration. Enjoy the rest of your Sunday.
```

Max Response 2
==============

* Removed html5 from doctype
* Reviewed working feature.
