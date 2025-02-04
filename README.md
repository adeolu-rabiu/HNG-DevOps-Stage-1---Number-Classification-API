# HNG Number Classification API - Stage 1 Assessment

## Overview
An API that classifies numbers based on mathematical properties and provides fun facts.

## Features
- Check if a number is **prime**, **perfect**, or **Armstrong**.
- Identify if it's **odd** or **even**.
- Calculate **digit sum**.
- Fetch a **fun fact** using the Numbers API.

## API Endpoint
**GET** `/api/classify-number?number=<integer>`

### Example Request
```bash
curl "http://18.135.29.41:5000/api/classify-number?number=371"

