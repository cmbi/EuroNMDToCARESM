#libraries

import hashlib
import urllib.parse
import requests
import random
import sys
import datetime

random.seed(1)

# Add Random Days
def addDays(baselineDate):
  dayAdded = random.randrange(100, 1000)
  baselineDate = datetime.datetime.strptime(baselineDate, "%Y-%m-%d")
  endDate = baselineDate + datetime.timedelta(dayAdded)
  return endDate.strftime("%Y-%m-%d")

# Create hashed EventID that is created with the 'date_of_assess_mm' + 'record_id' string
def createEventID(string: str, last_idx: int = 12) -> str:
  m = hashlib.md5()
  string = string.encode('utf-8')
  m.update(string)
  unqiue_name: str = str(int(m.hexdigest(), 16))[0:last_idx]
  return unqiue_name

def caresmModel(precare,
                #Possible Arguments in the model
                model='', pid='', event_id='', value='',
                age='', value_datatype='', valueIRI='',
                activity='', unit='', input='',
                target='', protocol_id='', frequency_type='',
                frequency_value='', agent='', startdate='',
                enddate='', comments=''):
  if not model or not pid:
    return precare
  templateModel = [model, pid, event_id, value, age,
                value_datatype, valueIRI, activity, unit,
                input, target, protocol_id, frequency_type,
                frequency_value, agent, startdate, enddate,
                comments]
  precare.append(templateModel)

  return precare


def sexProperty(dfRow, sexDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])
  # Add Ontology as a value datatype
  if 'female' == dfRow['sex_at_birth']:
    sexOnt = 'http://purl.obolibrary.org/obo/NCIT_C16576'
  elif 'male' == dfRow['sex_at_birth']:
    sexOnt = 'http://purl.obolibrary.org/obo/NCIT_C20197'
  else:
    sexOnt = 'http://purl.obolibrary.org/obo/NCIT_C124294'
  sexDataset = caresmModel(precare = sexDataset, model = 'Sex', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['sex_at_birth'],
                valueIRI= sexOnt,
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return sexDataset

def birthProperty(dfRow, birthDateDataset, birthYearDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])

  birthDateDataset = caresmModel(precare = birthDateDataset, model = 'Birthdate', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['date_of_birth'],
                value_datatype = 'xsd:date',
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  birthYearDataset = caresmModel(precare = birthYearDataset, model = 'Birthyear', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['date_of_birth'][0:4],
                value_datatype = 'xsd:integer',
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return birthDateDataset, birthYearDataset

def firstContactProperty(dfRow, firstContactDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])

  firstContactDataset = caresmModel(precare = firstContactDataset, model = 'First_visit', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['date_of_first_contact'],
                value_datatype = 'xsd:date',
                age = dfRow['age_at_baseline'],
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return firstContactDataset

def symptomsOnsetProperty(dfRow, symptomsOnsetDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])

  symptomsOnsetDataset = caresmModel(precare = symptomsOnsetDataset, model = 'Symptoms_onset', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['date_for_age_at_onset'],
                value_datatype = 'xsd:date',
                age = dfRow['age_at_baseline'],
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return symptomsOnsetDataset

def symptomsOnsetProperty(dfRow, symptomsOnsetDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])

  symptomsOnsetDataset = caresmModel(precare = symptomsOnsetDataset, model = 'Symptoms_onset', pid = dfRow['record_id'],
                event_id = eventIdval, value= dfRow['date_for_age_at_onset'],
                value_datatype = 'xsd:date',
                age = dfRow['age_at_baseline'],
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return symptomsOnsetDataset

def diagnosisProperty(dfRow, diagnosisDataset):
  eventIdval = createEventID(str(dfRow['date_of_assess_mm']) + dfRow['record_id'])
  
  # If no values, don't add anything
  if '"' in dfRow['diagnosis_rd_orpha']:
      return caresmModel(precare = diagnosisDataset)

  # Add undiagnosed values 10% of the time
  if random.random() > 0.9:

    diagnosisDataset = caresmModel(precare = diagnosisDataset, model = 'Diagnosis', pid = dfRow['record_id'],
              event_id = eventIdval, value= 'NCIT_C113725',
              value_datatype = 'xsd:string',
              age = '', 
              valueIRI = 'http://purl.obolibrary.org/obo/NCIT_C113725',
              startdate= dfRow['date_of_visit_bl'],
              enddate=dfRow['date_of_visit_bl'])
    return diagnosisDataset

  # If URI, add it
  if dfRow['diagnosis_rd_orpha_uri']:
    ontVal = dfRow['diagnosis_rd_orpha_uri']

  # Retrieve Label from URI
  if ontVal not in diagnosisTerms:
    ontValEncoded = urllib.parse.quote_plus(ontVal)
    ontValEncoded = urllib.parse.quote_plus(ontValEncoded)
    infoOnt = requests.get( 'https://www.ebi.ac.uk/ols4/api/terms/' + ontValEncoded)
    infoOnt = infoOnt.json()
    ontLabel = infoOnt['_embedded']['terms'][0]['label']
    diagnosisTerms[ontVal] = ontLabel
  else:
    ontLabel = diagnosisTerms[ontVal]
  ontLabel = ontLabel.replace(',', '')  # remove any unwanted ',' that can change the format of a CSV file

  # Calculate age
  ageDiagnosis = ''
  if dfRow['date_for_age_at_diagnosis'] and dfRow['date_of_birth']:
    dateDiagnosis =dfRow['date_for_age_at_diagnosis'].split('-')
    dateBirth = dfRow['date_of_birth'].split('-')
    ageDiagnosis = int(dateDiagnosis[0]) - int(dateBirth[0]) - ((int(dateDiagnosis[1]), int(dateDiagnosis[2])) < (int(dateBirth[1]), int(dateBirth[2])))

  diagnosisDataset = caresmModel(precare = diagnosisDataset, model = 'Diagnosis', pid = dfRow['record_id'],
                event_id = eventIdval, value= ontLabel,
                value_datatype = 'xsd:string',
                age = str(ageDiagnosis), 
                valueIRI = ontVal,
                startdate= dfRow['date_of_visit_bl'],
                enddate=dfRow['date_of_visit_bl'])
  return diagnosisDataset

def disabilityProperty(dfRow, disabilityDataset):
  for visit in range(random.randrange(2)):
    # Random day
    baselineDay = addDays(dfRow['date_of_assess_mm'])
    eventIdval = createEventID(str(baselineDay) + dfRow['record_id'])
    # Random disability score
    disabilityScore= random.randrange(1, 101)
    
    disabilityDataset = caresmModel(precare = disabilityDataset, model = 'Disability', pid = dfRow['record_id'],
                event_id = eventIdval,
                value = str(disabilityScore),
                activity = 'http://purl.obolibrary.org/obo/NCIT_C132531',
                value_datatype = 'xsd:integer',
                startdate = baselineDay,
                enddate = baselineDay)
  return disabilityDataset

def geneticProperty(dfRow, geneticDataset):
  for visit in range(random.randrange(1, 10)):
    # Random day
    baselineDay = addDays(dfRow['date_of_assess_mm'])
    eventIdval = createEventID(str(baselineDay) + dfRow['record_id'])
    # Random genetic data
    ## Choose which variant we add to the database
    variantNumber = random.randrange(0,3)
    listHGVS= ['NM_000232.5(SGCB):c.544A>G', 'NM_000232.5(SGCB):c.416G>A','NM_000337.6(SGCD):c.493C>T']
    listHGVSLink= ['https://www.ncbi.nlm.nih.gov/clinvar/variation/2203542/',
                  'https://www.ncbi.nlm.nih.gov/clinvar/variation/598036/',
                  'https://www.ncbi.nlm.nih.gov/clinvar/variation/8172/']
    geneticDataset = caresmModel(precare = geneticDataset, model = 'Genetic', pid = dfRow['record_id'],
                event_id = eventIdval,
                value = listHGVS[variantNumber],
                valueIRI = listHGVSLink[variantNumber],
                activity = 'http://purl.obolibrary.org/obo/NCIT_C18477',
                input = 'http://purl.obolibrary.org/obo/NCIT_C17610',
                agent = 'NCIT:Gene Variant',
                startdate = baselineDay,
                enddate = baselineDay)
    listHGNC= ['HGNC:10806', 'HGNC:10806', 'HGNC:10807']
    listHGNCLink= ['https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10806',
                  'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10806',
                  'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10807']
    geneticDataset = caresmModel(precare = geneticDataset, model = 'Genetic', pid = dfRow['record_id'],
                event_id = eventIdval,
                value = listHGNC[variantNumber],
                valueIRI = listHGNCLink[variantNumber],
                activity = 'http://purl.obolibrary.org/obo/NCIT_C18477',
                input = 'http://purl.obolibrary.org/obo/NCIT_C17610',
                agent = 'NCIT:Gene Variant',
                startdate = baselineDay,
                enddate = baselineDay)
    listOMIM= ['600900', '600900', '601411']
    listOMIMLink= ['https://www.omim.org/entry/600900', 'https://www.omim.org/entry/600900',
                  'https://www.omim.org/entry/601411']
    geneticDataset = caresmModel(precare = geneticDataset, model = 'Genetic', pid = dfRow['record_id'],
                event_id = eventIdval,
                value = listOMIM[variantNumber],
                valueIRI = listOMIMLink[variantNumber],
                activity = 'http://purl.obolibrary.org/obo/NCIT_C18477',
                input = 'http://purl.obolibrary.org/obo/NCIT_C17610',
                agent = 'NCIT:Gene Variant',
                startdate = baselineDay,
                enddate = baselineDay)

  return geneticDataset

def medicationProperty(dfRow, medicationDataset):
  for visit in range(random.randrange(1, 5)):
    # Random day
    baselineDay = addDays(dfRow['date_of_assess_mm'])
    eventIdval = createEventID(str(baselineDay) + dfRow['record_id'])
    # Random value with random decimals for medication
    decimals = random.randint(1, 4)
    value = random.uniform(0, 1000)
    valueMedication=round(value, decimals)

    medicationDataset = caresmModel(precare = medicationDataset, model = 'Medication', pid = dfRow['record_id'],
                event_id = eventIdval,
                value = str(valueMedication),
                activity = 'http://purl.obolibrary.org/obo/NCIT_C38114',
                value_datatype = 'xsd:float',
                unit = 'http://purl.obolibrary.org/obo/UO_0000000',
                protocol_id = 'https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1',
                frequency_type = 'http://purl.obolibrary.org/obo/NCIT_C21514',
                frequency_value = str(random.randrange(1,5)),
                agent = 'https://www.whocc.no/atc_ddd_index/?code=A07EA01',
                startdate = baselineDay,
                enddate = baselineDay)
  return medicationDataset

def phenotypeProperty(dfRow, phenotypeDataset):
  for visit in range(random.randrange( 5)): # Add from 1 to 5 Phenotype entries
    # Random day
    baselineDay = addDays(dfRow['date_of_assess_mm'])
    eventIdval = createEventID(str(baselineDay) + dfRow['record_id'])
    # List of possible HPO terms
    listHPO = ['http://purl.obolibrary.org/obo/HP_0003398',
              'http://purl.obolibrary.org/obo/HP_0003473',
              'http://purl.obolibrary.org/obo/HP_0030208',
              'http://purl.obolibrary.org/obo/HP_0100285',
              'http://purl.obolibrary.org/obo/HP_0003397']
    phenotypeDataset = caresmModel(precare = phenotypeDataset, model = 'Phenotype', pid = dfRow['record_id'],
                event_id = eventIdval,
                valueIRI = random.choice(listHPO),
                startdate = baselineDay,
                enddate = baselineDay)
  return phenotypeDataset

def retrieveCSVFormat(dataset, fileName):
  # Format data
  dataset = [','.join(dfrow) for dfrow in dataset]
  dataset = '\n'.join(dataset)
  # Add it as a new file
  header = ['model', 'pid', 'event_id', 'value', 'age', 'value_datatype', 'valueIRI',
           'activity', 'unit', 'input', 'target', 'protocol_id', 'frequency_type', 
           'frequency_value', 'agent', 'startdate', 'enddate', 'comments']
  newCSV = ','.join(header) + '\n'
  newCSV += dataset
  with open(f"{fileName}.csv", "w") as f:
    f.write(newCSV)

def main(df):

  # Initialise variables
  rownum=0
  sexDataset = list()
  birthDateDataset = list()
  birthYearDataset = list()
  firstContactDataset = list()
  symptomsOnsetDataset = list()
  diagnosisDataset = list()
  geneticDataset = list()
  disabilityDataset = list()
  medicationDataset = list()
  phenotypeDataset = list()

  # For every line in the EuroMD data
  for dfRow in df:
    rownum += 1
    dfRow= dfRow.strip().split(',')
    # Skip the header row
    if rownum == 1:
      header = dfRow
      continue

    # Add two values (variable name and value) from same position in two list as a key/value pair in a dict
    # Ex: list1 = ['x', 'y'], list2 = [1, 2] -> {'x': 1, 'y':2}
    dfDict = dict(zip(header, dfRow))

    # Mapping functions
    if dfDict['sex_at_birth']:
      sexDataset = sexProperty(dfDict, sexDataset)
    if dfDict['date_of_birth']:
      birthDateDataset, birthYearDataset = birthProperty(dfDict, birthDateDataset, birthYearDataset)
    if dfDict['date_of_first_contact']:
      firstContactDataset = firstContactProperty(dfDict, firstContactDataset)
    if dfDict['date_for_age_at_onset']:
      symptomsOnsetDataset = symptomsOnsetProperty(dfDict, symptomsOnsetDataset)
    if dfDict['diagnosis_rd_orpha_uri']:
      diagnosisDataset = diagnosisProperty(dfDict, diagnosisDataset)
    # Add synthetic data to the properties without data
    if dfDict['date_of_assess_mm']:
      disabilityDataset = disabilityProperty(dfDict, disabilityDataset)
      geneticDataset = geneticProperty(dfDict, geneticDataset)
      medicationDataset = medicationProperty(dfDict, medicationDataset)
      phenotypeDataset = phenotypeProperty(dfDict, phenotypeDataset)
    
    # Not needed now for the analysis
      # 'eodc_reason': Death information
      # Add Consent - Not possible in CARE-SM
      # Add Duplicate Patient IDs - Don't know how to do it

  # Write results in a file
  retrieveCSVFormat(sexDataset, 'Sex')
  retrieveCSVFormat(birthDateDataset, 'Birthdate')
  retrieveCSVFormat(birthYearDataset, 'Birthyear')
  retrieveCSVFormat(firstContactDataset, 'First_visit')
  retrieveCSVFormat(symptomsOnsetDataset, 'Symptoms_onset')
  retrieveCSVFormat(diagnosisDataset, 'Diagnosis')
  retrieveCSVFormat(disabilityDataset, 'Disability')    
  retrieveCSVFormat(geneticDataset, 'Genetic')
  retrieveCSVFormat(medicationDataset, 'Medication')
  retrieveCSVFormat(phenotypeDataset, 'Phenotype')
  
if __name__ == "__main__":
  #Import csv
  df = sys.argv[1]
  # Global Dict for Diagnosis terms
  diagnosisTerms = dict()
  with open(df, 'r') as csvfile:
    # Run script
    main(csvfile)