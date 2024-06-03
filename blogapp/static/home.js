let Toggle =false
function handleClick(event) {
Toggle =!Toggle
    const commentsSection = event.target.closest('.container').querySelector('.comments-section');
    commentsSection.classList.toggle('show-comments');
}

const commentButton = document.querySelectorAll('.comment-btn');
commentButton.forEach((item)=>{
    item.addEventListener('click', handleClick);
})

// const likeButton = document.querySelectorAll(".like-btn");
// likeButton.forEach((item) => {
//     item.addEventListener("click", handleBtnClick);
//     });

// let Like_togle = false
// function handleBtnClick(event)
// {
    
//     event.target.classList.toggle("like-btn-active");
//     Like_togle = !Like_togle
// }

