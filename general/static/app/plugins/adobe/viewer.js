(()=>{"use strict";var e={r:e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}},t={};e.r(t);const c=Object.freeze({latest:"2.35.2_3.1.3-d8cc32e2",public:"2.35.2_3.1.3-3ac6701a",legacy:"2.35.2_3.1.3-3ac6701a",edit:"2.24.4_2.12.0-7d0a8c15"});!function loadSDKScript(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"latest.js",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:c.latest,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"View",r=Array.from(document.scripts),i="view-sdk/".concat(e),a=r.find((function(e){return e.src&&e.src.endsWith(i)})).src,o=a.substring(0,a.indexOf(e)),d="".concat("".concat(o+t,"/").concat(n),"SDKInterface.js"),s=document.createElement("script");s.async=!1,s.setAttribute("src",d),document.head.appendChild(s)}("viewer.js",c.public),window.adobe_dc_view_sdk=t})();
