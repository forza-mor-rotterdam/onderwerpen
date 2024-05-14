import { Controller } from '@hotwired/stimulus'
import { visit } from '@hotwired/turbo'
export default class extends Controller {
  connect() {
    window.addEventListener('popstate', () => {
      const overviewElement = document.querySelector('#overview')
      if (overviewElement) {
        const overviewSrcAttr = overviewElement.getAttribute('src')
        if (overviewSrcAttr) {
          const urlPath = overviewSrcAttr.split('?')[0] + window.location.search
          visit(urlPath, { frame: 'overview' })
        }
      }
    })
  }
}
