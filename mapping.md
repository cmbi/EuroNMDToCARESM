# Euro-NMD to CARE-SM Mapping Documentation

This file shows the mapping between the [Euro-NMD codebook](https://zenodo.org/records/11931376) and the [CARE-SM Model](https://care-sm.readthedocs.io/en/latest/glossary.html#csv-template-creation). As the mapping is between a codebook and a semantic model, the conversion is never 1-to-1. Instead, one data element in CARE-SM with multiple properties can have multiple variables from the Euro-NMD codebook.

The data elements that are can't be mapped and are needed to have a complete implementation of CARE-SM have been added with synthetic data.

## Data Element Glossary

* Demographics:
    * [Birthdate](#birthdate)
    * [Birthyear](#birthyear)
    * [Sex](#sex)

* Participation and Timeline:
    * [First_visit](#first-visit)
    * [Symptoms_onset](#symptoms-onset)

* Conditions and findings:
    * [Diagnosis](#diagnosis)

**Legend:**

- ![](https://placehold.co/15x15/808080/808080.png) This column is **UNUSED** for this case.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) This column is filled in **IN CASE OF ANY**.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) This column colored is **REQUIRED** for this case.

Here you can find the list of data elements and the columns required to be defined. Those that are optional, feel free to add them. If not, leave them empty.
<hr>

### Birthdate

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthdate.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: `date_of_birth` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

### Birthyear

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthyear.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Only first 4 digits (YYYY) of `date_of_birth` from Euro-NMD.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

### Sex

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Sex.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: `sex_at_birth` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: one of the following: 
    * http://purl.obolibrary.org/obo/NCIT_C16576 (Female) ; 
    * http://purl.obolibrary.org/obo/NCIT_C20197 (Male); 
    * http://purl.obolibrary.org/obo/NCIT_C124294 (Undetermined) ; 
    * http://purl.obolibrary.org/obo/NCIT_C17998 (Unknown, use this for foetal undetermined) 
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

### First Visit

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: First_visit
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: `date_of_first_contact` from Euro-NMD codebook. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**: `age_at_baseline` from Euro-NMD codebook. 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

### Symptoms onset

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Symptoms_onset
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: `date_for_age_at_onset` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: `xsd:date`
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**: 
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**: `age_at_baseline` from Euro-NMD codebook. 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

### Diagnosis

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Diagnosis
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: `record_id` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **value**: Human readable label of the diagnosed condition. Ex: Extract the label from  https://www.ebi.ac.uk/ols4/api/terms/' + `diagnosis_rd_orpha_uri` in a programatic way. 
- ![](https://placehold.co/15x15/808080/808080.png)  **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: `diagnosis_rd_orpha_uri` from Euro-NMD codebook.
- ![](https://placehold.co/15x15/808080/808080.png)  **activity**:
- ![](https://placehold.co/15x15/808080/808080.png)  **unit**:
- ![](https://placehold.co/15x15/808080/808080.png)  **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **target**:
- ![](https://placehold.co/15x15/808080/808080.png)  **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png)  **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: `date_of_visit_bl` from Euro-NMD. Ensure ISO 8601 format date.
- ![](https://placehold.co/15x15/808080/808080.png) **age**: `age_at_baseline` from Euro-NMD codebook. 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Identificator for the event based of the `date_of_assess_mm` and `record_id`.
<hr>

**Note: [CARE-SM CSV Glossary Documentation](https://care-sm.readthedocs.io/en/latest/glossary.html#csv-template-creation) serves as the base style of this file**