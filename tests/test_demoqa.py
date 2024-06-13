from selene import browser
import os


def test_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('ivanivanov@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('89123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="5"]').click()
    browser.element('.react-datepicker__year-select option[value="1994"]').click()
    browser.all('.react-datepicker__day--003').second.click()
    browser.element('#subjectsInput').type('English')
    browser.element('.subjects-auto-complete__menu').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('.form-file').click().element('#uploadPicture').send_keys(os.path.abspath('images.jpeg'))
    browser.element('#currentAddress').type('Страна, город, улица, дом, этаж, квартира')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()
