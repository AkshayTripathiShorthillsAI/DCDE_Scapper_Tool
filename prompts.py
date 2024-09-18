# prompts.py

GENERAL_PROMPT = '''You are an scrapper for a website. Given a long text, extract and return only json:

Manufacturer: Identify the name of the company or brand that produces the product.
Model: Find the specific model name or number associated with the product.
Year: Determine the manufacturing year or the model year for the product.
MSRP (Manufacturer's Suggested Retail Price): Extract the suggested retail price if mentioned, otherwise indicate if it's not provided.
Category: Identify the general category or type of product (e.g., Forklifts, Lift Trucks).
Subcategory: Find any subcategory or specific type within the general category (e.g., Walkie Straddle Stacker).
Description: Extract a brief description or overview of the product, highlighting its key features and uses.
Countries: List the countries where the product is available or mentioned.

long text:{long_text}

json:
"general": 
      "manufacturer": "",
      "model": "",
      "year": 2024,
      "msrp": 0,
      "category": "",
      "subcategory": "",
      "description": "",
      "countries": ["USA","CA"]
'''


FEATURES_PROMPT = '''Return the features of vehicle.It may include the following details:

Engine Performance: Details about the engine type, horsepower, torque, and fuel efficiency.
Transmission: Information on the type of transmission (automatic, manual, CVT) and its features.
Interior Features: Descriptions of comfort features like seating materials, infotainment systems, climate control, and cabin space.
Safety Features: Information on safety systems such as airbags, anti-lock brakes, stability control, and driver-assistance technologies.
Exterior Features: Details about exterior design elements, lighting, wheel size, and paint options.
Technology: Features related to connectivity, navigation systems, and advanced driver-assistance systems (ADAS).
Convenience: Features that enhance user convenience like keyless entry, power windows, and adjustable mirrors.
Cargo Capacity: Information on the space available for cargo and storage solutions.
Fuel Efficiency: Data on the vehicle’s fuel economy and emissions.
Warranty and Maintenance: Information about the warranty coverage and maintenance packages.

long text:{long_text}
'''

DIMENSION_PROMPT = '''You have been given a long text. Your task is to extract specific dimensional specifications and convert them into a JSON format. For each attribute listed below, provide the "label" and "desc" using the format shown. Ensure that the extracted data is concise and accurately reflects the information provided in the text.

Format:
"attribute": {{
  "label": "Attribute Label",
  "desc": "Attribute Description"
}}

Attributes to extract:
- mastType
- loadCenter
- wheelbase
- wheelSizeFrontDXWPoly
- wheelSizeFrontDXWRubber
- wheelSizeRearDXWPoly
- wheelSizeRearDXWSteel
- additionalWheelsCasterWheelDXWPoly
- trackWidthRear
- liftHeight
- freeLift
- collapsedHeight
- extendedHeightWOLoadBackrest
- extendedHeightWLoadBackrest
- loadBackrestWidthLoadBackrestHeightInHigh
- tillerArmHeightInDrivePositionMinMax
- outriggerHeight
- loweredForkHeight
- powerUnitHeight
- forkLengths
- forkDimensionsThicknessXWidth
- widthAcrossForksAdjustableMinMaxWithoutForkLocks
- widthAcrossForksAdjustableMinMaxWithForkLocks
- headlengthWithoutForkLocks
- headlengthWithForkLocks
- overallLength
- insideStraddle
- overallWidthFront
- overallWidthRear
- forkCarriageWidth
- groundClearanceWLoadBelowMast
- groundClearanceCenterWheelbase
- turningRadius
- lengthWOutriggers
- maximumBatteryBoxLXWXH

Long text: {long_text}
'''

OPERATIONS_PROMPT = """You have been given a long text. Your task is to extract specific operational specifications and convert them into a JSON format. For each attribute listed below, provide the "label" and "desc" using the format shown. Ensure that the extracted data is concise and accurately reflects the information provided in the text.

Format:
"attribute": {{
  "label": "Attribute Label",
  "desc": "Attribute Description"
}}

Attributes to extract:
- Manufacturer
- Power
- Operator Type
- Load Capacity
- Weight (Less Battery)
- Wheels Number (X-Driven, Front/Rear)
- Capacity at Lift Height (mm, LC)
- Capacity at Lift Height (One, mm, LC)
- Capacity at Lift Height (Two, mm, LC)
- Capacity at Lift Height (Three, mm, LC)
- Travel Speed (Without Load)
- Lift Speed (Without Load)
- Lowering Speed (Without Load)
- Gradeability (Without Load, One, Min Rating)
- Gradeability (Without Load, Min Rating)
- Gradeability (Without Load, Two, Min Rating)
- Service Brake
- Type of Controller/Drive

Long text: {long_text}
"""