/**
 * Created by Maxwell J. Resnick on 8/28/15.
 */
// Globals - ewww
var gallery = document.getElementById('gallery');
var anAnnoyingModal = document.getElementById('image_show');

function modalClick(target) {
    this.target = target;
    // user clicked outside of the modal, because our target is the div.
    if (this.target.id === 'image_show') {
        this.target.className = "display_none";
    }
}

function galleryClick(target) {
    this.target = target.getAttribute('src');
    this.oldImage = anAnnoyingModal.getElementsByTagName('img')[0];
    anAnnoyingModal.removeChild(this.oldImage);
    this.newImage = document.createElement('img');
    this.newImage.setAttribute('src', this.target);
    anAnnoyingModal.appendChild(this.newImage);
    // one will never misspell this again.
    anAnnoyingModal.className = 'display_img';
}

// One Time Page Creation Stuffs
var imageArray = (function () {
    /*
     * @description we build an array of all the image filenames.
     *  DRY fail from index.js X_x
     */
    this.images = [];
    for (var i = 0; i < 60; i++) {
        this.num = i+1;
        this.filePrefix = "images/pdxcg_";
        this.filePostfix = ".jpg";
        // we add a "0" but also just cast everything to string
        if (this.num < 10) {
            this.num = "0" + this.num.toString();
        } else {
            this.num = this.num.toString();
        }
        this.fullPath = this.filePrefix + this.num + this.filePostfix;
        this.images.push(this.fullPath);
    }
    return this.images;
}());

// paint the page with the gallery magic.
var paintGallery = (function (){
    /*
     * @description we "paint" html all over the place w/ out images.
     */
    // <li><img src="images/pdxcg_01.jpg" /></li>
    for (var i=0; i<imageArray.length; i++) {
        this.bullet = document.createElement('li');
        this.image = document.createElement('img');
        this.image.setAttribute('src', imageArray[i]);
        this.bullet.appendChild(this.image);
        gallery.appendChild(this.bullet);
    }
}());


// set username
var setUserName = (function (){
    /*
     * @description we set our username once, and forget it.
     */
    this.tagline = document.getElementsByClassName('tagline')[0];
    this.username = sessionStorage.getItem('javapic');
    this.tagline.textContent = "develop something beautiful " + this.username;
}());

anAnnoyingModal.addEventListener('click', function(e){
    modalClick(e.target);
});
// Event Handlers
gallery.addEventListener('click', function(e){
   galleryClick(e.target);
});
