# Code-related Todo's
## Todo
### Essentials
- [ ] Scan Claim Policy and save it on MongoDB
    - pagination for multiple invoices in 1 claim
    - temperature 0
- [ ] add loading animation (isLoading in Pinia) for different page
- [ ] rework claim policy input fields (use AI then real admin validates)

### Nice to have
- [ ] Pagination
    - [ ] Claim center
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
- [-] Create Pinia store to prepare end-to-end
      - then replace all repeated data in different pages
```
.
├── backend
│   ├── requirements.txt
│   └── myvenv
├── frontend
│   └── package.json
└── README.md
```

## To be added on Teamhub
Small Fix: Date sort in admin claim fix
refer to employee claim

Small Fix: Item number/quantity in admin claim fix

plan API for admin dashboard

plan API for ask claimsy

Final remove every link in navbar when login
