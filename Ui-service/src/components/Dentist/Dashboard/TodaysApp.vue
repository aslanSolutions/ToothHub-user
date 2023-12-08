<template>
  <div class="dentist-t">
    <h1 class="text-3xl md:text-3xl leading-24 md:leading-32 font-inter font-semibold tracking-tighter text-cyan-800 dark:text-cyan-600">
      Today’s Appointments
    </h1>

    <div class="group">
      <div class="square-container">
        <div class="square">
          <div class="flex-container">
            <div class="ellipse" id="ellipse806"></div>

            <div class="flex-item text-info-container">
              <div class="text-info">
                <div class="name">
                  Roisin Durham
                </div>
                <div class="email">
                  RoisinDurham@gmail.com
                </div>
                <div class="time">
                  13:00 PM
                </div>
                <div class="dental-implant">
                  Dental Implant
                </div>
              </div>
            </div>
          </div>

          <div class="button-container">
            <button class="view-details-btn">View Details</button>
          </div>
        </div>
        <div class="square">
          <div class="flex-container">
            <div class="ellipse" id="ellipse807"></div>

            <div class="flex-item text-info-container">
              <div class="text-info">
                <div class="name">
                  John Doe
                </div>
                <div class="email">
                  john.doe@example.com
                </div>
                <div class="time">
                  14:30 PM
                </div>
                <div class="dental-implant">
                  Tooth Extraction
                </div>
              </div>
            </div>
          </div>

          <div class="button-container">
            <button class="view-details-btn">View Details</button>
          </div>
        </div>
        <div class="square">
          <div class="flex-container">
            <div class="ellipse" id="ellipse808"></div>

            <div class="flex-item text-info-container">
              <div class="text-info">
                <div class="name">
                  Jane Smith
                </div>
                <div class="email">
                  jane.smith@example.com
                </div>
                <div class="time">
                  15:45 PM
                </div>
                <div class="dental-implant">
                  Checkup
                </div>
              </div>
            </div>
          </div>

          <div class="button-container">
            <button class="view-details-btn">View Details</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style lang="scss">
  .square-container {
    display: flex;
    flex-direction: row;
    margin: 1rem;
    gap: 10rem;
  }

  .flex-container {
    display: flex;
    flex-direction: row;
  }

  .appointments {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 61px;
    color: #4987A1;
    width: 100%;
    text-align: end;
    margin-right: 30rem;
  }

  .view-details-btn {
    width: 18rem;
    background-color: #4987a1;
    border-radius: 1.5rem;
    color: #fff;
    margin-top: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  .view-details-btn:hover {
    background-color: #346e8a;
  }

  .square {
    width: 18rem;
    height: auto;
    border: 0.5px solid rgba(163, 163, 163, 0.05);
    border-radius: 1.5rem;
    margin-right: 1rem;
  }

  .ellipse {
    width: 100px;
    height: 100px;
    border-radius: 78px;
    background: url('~@/assets/Guy.png') center/cover;
  }

  .flex-item {
    margin-top: 0.5rem;
  }

  .name,
  .email,
  .time,
  .view-details-btn,
  .dental-implant {
    font-family: 'Inter';
    font-style: normal;
  }

  .view-details-btn {
    font-weight: 700;
  }

  .name {
    font-weight: 600;
    font-size: 15px;
    line-height: 24px;
    color: #000000;
  }

  .email {
    font-weight: 400;
    font-size: 10px;
    line-height: 14px;
    color: #B7B7B7;
  }

  .time {
    font-weight: 400;
    font-size: 15px;
    line-height: 24px;
    color: #B7B7B7;
  }

  .dental-implant {
    font-weight: 600;
    font-size: 15px;
    line-height: 24px;
    color: #B7B7B7;
  }
</style>
