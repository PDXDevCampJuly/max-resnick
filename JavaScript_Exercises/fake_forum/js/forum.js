/**
 * Created by Max Resnick 9/8/15
 * @description forum javascript
 */


// Load no conflict version
var $jQ = jQuery.noConflict();
var posts = []; // all our posts.


// Objects
var httpService = {
    /*
     * @description HTTP request handler
     * @return HTTP request as promise
     */
    "get": function () {
        return $jQ.ajax({
            type: "GET",
            dataType: "jsonp",
            url: "https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
        });
    },
    "post": function (title, body) {
         var _data = {
            entry_434124687: title,
            entry_1823097801: body,
         };
         return $jQ.ajax({
            type: "POST",
            url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
            dataType: 'json',
            data: _data,
         });
        }
    };

function forumPost (postTitle, postBody) {
    /*
     * @description object for a single forum post.
     */
    this.postTitle = postTitle;
    this.postBody = postBody;
    this.postHTML = (function () {
                    /*
                     * @description html for object.
                     */
                     return ('<div class="post"><h2>' +
                                        postTitle + '</h2><p>' +
                                        postBody + '</p></div>');
                    }());

}


function formHandler() {
    /*
     * @description determine if new post is valid, if so post to google docs.
     */
    var isValid = true;
    var $inputFields = $jQ('#post-body, #post-title');
    $inputFields.each(function(index, field) {
        // We are only foolishly checking if we're posting blank messages
        var fieldValue = field.value;
        if (fieldValue.length === 0 ) {
            isValid = false;
        }
    });
    if (isValid) {
        var title = $inputFields.get(0);
        var body = $inputFields.get(1);
        httpService.post(title.value, body.value)
                         .then(function(data) {
                            // success function
                            console.log(data);
                         }, function(data){
                            // error function
                            // hack since we have a cross origin, error, now we add a new forum post
                            var newPost = new forumPost(title.value, body.value);
                            posts.push = newPost;
                            renderPosts(newPost);
                            // reset form.
                            title.value = "";
                            body.value = "";
                         });
    }
    // TODO handle error messaging.
}

function renderPosts(postsToRender) {
    /*
     * @param postsToRender [array] objects to render.
     * @description renders forum posts on html.
     */
    var $main = $jQ('main');
    console.log(postsToRender);
    $jQ(postsToRender).each(function(index, formPost) {
            $main.append(formPost.postHTML);
    });
}

// Event binding
$jQ(function () {
    /*
     * @description bind to submit button on page load.
     */
    $jQ('#new-post').on({
        'submit': function(e) {
            e.preventDefault();
            formHandler();
        },
    });
});


// On Load functions
(function () {
    /*
     * @description load all posts on a page load.
     */
    httpService.get().then(function(data) {
        data.feed.entry.forEach(function(entry){
            posts.push(new forumPost(entry.gsx$posttitle.$t, entry.gsx$postbody.$t));
        });
        renderPosts(posts);
    });

}());
