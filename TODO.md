# Code-related Todo's
## Todo
### Feedbacks
- [ ] john: smart suggest get it done to impress

- [ ] john: invoice/edit (both first and \[id]) table become input to edit (delete button)
- [ ] john: invoice/edit (both first and \[id]) unit next to quantity

### Essentials
- [ ] Smart Suggest feature
- [ ] seeder for anomaly
- [ ] fix unsubmitted invoice 10-15 invoices
- [ ] invoice/edit connect backend data
- [ ] seeder for fix employee demo data (using previous mock data)
- [ ] seeder for employee id 1 name
- [ ] seeder for fix chat data
- [ ] Chatbot feature
    - connect with backend, use fake data
    - just for employee 1

### Nice to have
- [ ] fuzzy search button
- [ ] Pagination
    - [ ] Claim center (10 claims per page)
    - [ ] Receipt upload (support multiple invoices at once)
- [ ] Notifications
- [ ] export data into pdf or csv
- [ ] More sorting
    - [ ] pending status in all claims
    - [ ] Total (RM)
- [ ] testing

## Done
- [x] john: submit button in invoice same column as checkbox
- [x] chee tat: category in my invoices (make it click)
- [x] john: upload receipt, show image (a lot = carousell)
- [x] john: navbar middle and to the sides (absolute and relative)
- [x] fix claim totalAmount in seeder
- [x] Claim has one or many invoice db table and database fix
- [x] Create `.env.example` and `.env`
- [x] create end-to-end project structure
- [x] Create Pinia store to prepare end-to-end
      - then replace all repeated data in different pages
- [x] Scan Claim Policy and save it on MongoDB
    - pagination for multiple invoices in 1 claim
    - temperature 0
- [x] add loading animation (isLoading in Pinia) for different page
- [x] rework claim policy input fields (use AI then real admin validates)

```
.
├── backend
│   ├── requirements.txt
│   └── myvenv
├── frontend
│   └── package.json
└── README.md
```

## Chatbot notes
- save all previous convo history
- convo history
    - employee_id
    - history: []{ isBotText: boolean text: string }
    - title
    - summary

- display old convo
- pass summary into new bot
- bot understand from summary

- answer anything according to the mongodb policy
- summary as context
- check how to save history in previous slides

## To be added on Teamhub
Small Fix: Date sort in admin claim fix
refer to employee claim

Small Fix: Item number/quantity in admin claim fix

plan API for admin dashboard

plan API for ask claimsy

Final remove every link in navbar when login
