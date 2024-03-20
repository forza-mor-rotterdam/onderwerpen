import { Controller } from '@hotwired/stimulus'

let form = null
let inputList = null
// eslint-disable-next-line no-unused-vars
let formData = null
const defaultErrorMessage = 'Vul a.u.b. dit veld in.'

export default class extends Controller {
  static values = {
    formIsSubmitted: Boolean,
    parentContext: String,
    standaardafhandelteksten: String,
  }
  static targets = ['externalText', 'internalText']

  connect() {
    if (this.hasExternalTextTarget) {
      if (this.externalTextTarget.textContent.length > 0) {
        this.externalMessage = this.externalTextTarget.textContent
      }
    }

    form = document.querySelector('#afhandelForm')
    inputList = document.querySelectorAll('.js-validation textarea')
    formData = new FormData(form)

    for (const input of inputList) {
      const error = input.closest('.form-row').getElementsByClassName('invalid-text')[0]
      input.addEventListener('input', () => {
        if (input.validity.valid) {
          input.closest('.form-row').classList.remove('is-invalid')
          error.textContent = ''
        } else {
          error.textContent = defaultErrorMessage
          input.closest('.form-row').classList.add('is-invalid')
        }
      })
    }

    form.addEventListener('submit', (event) => {
      const allFieldsValid = this.checkValids()

      if (!allFieldsValid) {
        const errorList = document.querySelectorAll('div.is-invalid')
        errorList[0].scrollIntoView({ behavior: 'smooth' })
        event.preventDefault()
      }
    })
  }

  checkValids() {
    // Check all input fields (except checkboxes) for validity
    // If one or more fields are invalid, don't send the form (return false)
    const inputList = document.querySelectorAll('[type="text"], [type="radio"], select, textarea')
    let count = 0
    for (const input of inputList) {
      const error = input.closest('.form-row').getElementsByClassName('invalid-text')[0]
      if (input.validity.valid) {
        error.textContent = ''
        input.closest('.form-row').classList.remove('is-invalid')
      } else {
        error.textContent = defaultErrorMessage
        input.closest('.form-row').classList.add('is-invalid')
        count++
      }
    }
    return count === 0
  }

  cancelHandle() {
    this.element.dispatchEvent(
      new CustomEvent('cancelHandle', {
        detail: JSON.parse(this.parentContextValue),
        bubbles: true,
      })
    )
  }

  setExternalMessage(evt) {
    if (this.hasExternalTextTarget) {
      this.choice = evt.params.index
      this.externalMessage = JSON.parse(this.standaardafhandeltekstenValue)[evt.target.value]
      this.externalTextTarget.value = this.externalMessage
    }
  }

  defaultExternalMessage() {
    if (this.externalMessage.length === 0) return

    this.externalTextTarget.value = this.externalMessage
  }

  clearExternalMessage() {
    this.externalTextTarget.value = ''
  }
}
