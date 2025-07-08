# Code-related Todo's
## Todo
### Essentials
- [ ] Smart Suggest feature
- [ ] seeder for fix chat data
- [ ] Chatbot feature
    - connect with backend, use fake data
    - just for employee 1

### Nice to have
- [ ] Pagination
    - [ ] Claim center (10 claims per page)
    - [ ] Receipt upload (support multiple invoices at once)
- [ ] Notifications
- [ ] export data into pdf or csv
- [ ] More sorting
    - [ ] pending status in all claims
    - [ ] Total (RM)

## Done
- [x] Claim has one or many invoice db table and database fix
- [x] Setup database and create seeder
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
