/**
 * Created by Max Resnick 9/8/15
 * @description forum javascript
 */


// Load no conflict version
var $jQ = jQuery.noConflict();
var posts = []; // all our posts.



var httpService = {
    /*
     * @description return a HTTP request as a promise
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
     * @description object handles a single forum post.
     */
    this.postTitle = postTitle;
    this.postBody = postBody;
    this.newPost = (function () {
                     var thepost = ('<div class="post"><h2>' +
                                        postTitle + '</h2><p>' +
                                        postBody + '</p></div>');
                     $jQ('.post').last().after(thepost);
                    }());

}

function loadPosts(data) {
    /*
     * @param [array] posts to add.
     * @description creates new forumPost object given an array of posts.
     */
    data.forEach(function(entry){
        posts.push(new forumPost(entry.gsx$posttitle.$t, entry.gsx$postbody.$t));

    });
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
                         }, function(stuff){
                            // hack since we have a cross origin, error
                            posts.push = new forumPost(title.value, body.value);
                         });
        // reset form.
        title.value = "";
        body.value = "";
    }
}

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

(function () {
    /*
     * @description load all posts on a page load.
     */
    httpService.get().then(function(data) {
        loadPosts(data.feed.entry);
    });

}());
