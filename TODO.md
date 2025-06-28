# Code-related Todo's
## Todo
### Essentials
- [ ] add isLoading to Pinia
- [ ] rework claim policy input fields (use AI then real admin validates)
    - pagination for multiple invoices in 1 claim
    - temperature 0

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
Fix: Date sort in admin claim fix
Fix: Item number in admin claim fix

Page to re-evaluate claim status
go back into admin claim review again

separate employee and admin's ask-claimsy
employee/ask-claimsy
admin/ask-claimsy

plan API for admin dashboard

plan API for ask claimsy

remove every link in navbar when login
