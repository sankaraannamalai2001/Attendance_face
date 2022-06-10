# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:29:43 2021

@author: kalya
"""

import enroll,spreadsheet,emailing,recognition
recognition.load_facial_encodings_and_names_from_memory()

spreadsheet.mark_all_absent()

recognition.run_recognition()



# enroll.enroll_via_camera('jeeva')
# enroll.enroll_via_camera('paulson')
# enroll.enroll_via_camera('raj')
# enroll.enroll_via_camera('sankar')
# enroll.enroll_via_camera('prathish')
# enroll.enroll_via_camera('srinivasan')
# enroll.enroll_via_camera('selva')
#spreadsheet.enroll_person_to_sheet('kalyan','kalyan.plmr@gmail.com')

#emailing.email_pin('xxxx@gmail.com',1234)

#