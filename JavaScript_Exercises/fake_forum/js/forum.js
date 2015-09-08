/**
 * Created by Max Resnick 9/8/15
 * @description forum javascript
 */


function grr (data) { console.log("the string:");}
// Load noconflict version
var $jQ = jQuery.noConflict();
var httpService = {
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
             }
             return $jQ.ajax({
                type: "POST",
                url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
                dataType: 'json',
                data: _data,
             });
            }
        };

function addPost (postTitle, postBody) {
    var $lastPost = $jQ('.post');
    var forumPost = ('<div class="post"><h2>' +
                    postTitle + '</h2><p>' +
                    postBody + '</p></div>');
    $lastPost.last().after("<h2>stuff</h2>");
}
