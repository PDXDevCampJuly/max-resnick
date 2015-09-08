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

(function () {
    /*
     * @description load all posts on a page load.
     */
    httpService.get().then(function(data) {
        loadPosts(data.feed.entry);
    });

}());
