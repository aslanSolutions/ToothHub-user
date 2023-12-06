<template>
    <div class="message-box">
        <textarea
            required
            class="textarea"
            name="message"
            id="message"
            cols="30"
            rows="20"
            placeholder="write your message..."
        ></textarea>
        <button>Send</button>
    </div>
</template>

<style lang="scss" scoped>
.message-box {
    font-size: 17px;
    line-height: 23px;
    color: rgba(136, 135, 143, 1);
    width: 90%;
    padding-right: 20%;
}

button {
  padding: 10px 20px;
  background-color:  rgba(73, 135, 161, 1);
  border-radius: 10px;
  color:rgba(255, 255, 255, 1);
  border: none;
  cursor: pointer;
  width: 200px;
  margin-top: 30px;
}

button:hover {
  background: rgb(255, 162, 0);
}

.textarea{
    width: 90%;
    height: 70%;
    border-radius: 10px;
    font-size: inherit;
    outline-color: rgba(73, 135, 161, 1);
    padding: 20px;
    min-height: 100px;
    resize: vertical;
    max-height: 400px;
    min-height: 200px;
}

@media (max-width: 768px) {
  .message-box {
    font-size: 13px;
    line-height: 17px;
  }
}
</style>
