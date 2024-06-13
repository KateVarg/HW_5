from selene import browser, have
import os


def test_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('ivanivanov@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8912345678')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="5"]').click()
    browser.element('.react-datepicker__year-select option[value="1994"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--015').click()
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

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            'Иван Иванов',
            'ivanivanov@test.com',
            'Male',
            '8912345678',
            '15 June,1994',
            'English',
            'Reading, Music',
            'images.jpeg',
            'Страна, город, улица, дом, этаж, квартира',
            'NCR Gurgaon',
        )
    )