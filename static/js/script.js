$(document).ready(function() {
    debugger;
});

function AddUpvote(id) {
    
    var link = document.getElementById('upvote_'.concat(id)).src;
    var votes = parseInt(document.getElementById('rating_num_'.concat(id)).innerHTML);

    if (link.includes('grey')){
        link = link.replace('grey', 'clicked');
        votes+=1;
    }

    else {
        if (link.includes('clicked')){
            link = link.replace('clicked', 'grey');
            votes-=1;
        }
    }

    document.getElementById('upvote_'.concat(id)).src = link;
    document.getElementById('rating_num_'.concat(id)).innerHTML = votes;

}