# PayLink – Requirements Document

# 1. Introduction

## 1.1 Problem Summary

PayLink is an Egyptian digital payment platform that allows customers to pay their utility bills, including electricity, water, mobile top-ups, and internet bills, using a digital wallet. Customers can use the mobile application or visit authorized agents to complete their payments.

The main problem PayLink aims to solve is the difficulty and inconvenience of paying bills through traditional methods. Customers want a fast and reliable way to pay their bills without visiting utility offices or waiting in queues. At the same time, biller companies need to receive payments accurately and efficiently.

PayLink also faces important technical and business challenges. Since it manages customers' money through digital wallets, it must prevent duplicate charges, incorrect balance calculations, and charging customers for payments that billers have not received.

The system must support different billers that use different communication protocols, handle payment failures and delayed confirmations, maintain accurate transaction records, and provide reliable notifications.

Additionally, PayLink generates revenue through service fees and pays commissions to agents who complete payments on behalf of customers.

Therefore, the goal of this project is to develop a reliable, secure, and extensible backend system that manages digital wallets and bill payments accurately, supports multiple billers, handles different payment scenarios, and maintains accurate financial records.

## 1.2 Stakeholders

| Stakeholder | Role / Interest in the System | Main Needs and Expectations |
|---|---|---|
| Customers | Use the PayLink mobile application to pay electricity, water, mobile top-up, and internet bills using their digital wallets. | Convenient and reliable payments, accurate bill amounts and fees, correct wallet balances, and clear payment confirmations. |
| Agents | Use PayLink terminals in small shops to make payments on behalf of customers. | A reliable payment process, accurate transaction records, and correct calculation of agent commissions. |
| Biller Companies | Provide utility services and receive payments through PayLink integrations, including electricity, water, mobile, and internet providers. | Receive payments accurately and efficiently, with reliable communication and transaction information. |
| PayLink Management / Admin | Owns and manages the PayLink business and defines its business objectives. | Customer satisfaction, operational reliability, service-fee revenue, and the ability to support additional billers. |
| Engineering / Development Team | Designs, develops, tests, deploys, and maintains the PayLink backend system. | Clear requirements, maintainable architecture, reliable integrations, and effective testing and deployment processes. |
| Regulators | External parties that may oversee PayLink's handling of customers' money and financial records. | Responsible handling of funds and accurate, trustworthy financial records. |
| Support Employees | Handle customer inquiries, investigate payment issues, search transaction records, and manage account restrictions. | Accurate transaction information, clear payment histories, and effective tools for resolving customer issues. |

# 2. Functional Requirements – User Stories

## FR-1: Customer Registration

**Priority:** Must

**User Story:**

As a customer, I want to register for a PayLink account so that I can use the platform's bill payment and wallet services.

**Acceptance Criteria:**

- Given a visitor provides all required registration information, when they submit the registration form with valid information, then the system creates a new customer account with a Basic verification level.
- Given a visitor attempts to register using information that is already associated with an existing account, when they submit the registration form, then the system rejects the registration and displays an appropriate error message.
- Given a visitor provides invalid or incomplete registration information, when they submit the registration form, then the system displays validation errors and does not create the account.

## FR-2: Upgrade to Verified Account

**Priority:** Should

**User Story:**

As a customer, I want to upgrade my account to a Verified level so that I can benefit from higher daily payment limits.

**Acceptance Criteria:**

- Given a customer has a Basic account, when the customer successfully completes the required verification process, then the system upgrades the account to Verified.
- Given a customer has a Verified account, when the customer views their account information, then the system displays their Verified status and the applicable daily payment limit.
- Given a customer has not completed the required verification process, when they attempt to upgrade their account, then the system does not upgrade the account.

## FR-3: View Wallet Balance and Transaction History

**Priority:** Must

**User Story:**

As a customer, I want to view my wallet balance and transaction history so that I can monitor my available funds and previous transactions.

**Acceptance Criteria:**

- Given a customer is logged into their account, when they open the wallet section, then the system displays their available balance and held balance.
- Given a customer has previous wallet transactions, when they open their transaction history, then the system displays their recorded transactions.
- Given a customer has no previous transactions, when they open their transaction history, then the system displays an appropriate message indicating that no transactions are available.

## FR-4: Wallet Top-Up

**Priority:** Must

**User Story:**

As a customer, I want to add money to my wallet using a simulated card payment or agent cash so that I can use the balance to pay bills.

**Acceptance Criteria:**

- Given a customer has a valid simulated card payment, when they submit a valid top-up request, then the system adds the top-up amount to their wallet balance.
- Given a customer visits an authorized agent to add money, when the agent successfully processes the cash top-up, then the system credits the customer's wallet with the specified amount.
- Given a top-up request fails, when the system processes the request, then the system does not increase the customer's wallet balance.

## FR-5: Wallet Ledger

**Priority:** Must

**User Story:**

As a system administrator, I want every wallet balance change to be recorded in a ledger so that all financial transactions can be accurately tracked.

**Acceptance Criteria:**

- Given a wallet balance changes because of a transaction, when the transaction is successfully processed, then the system creates a corresponding ledger entry.
- Given a wallet has multiple ledger entries, when the system calculates its balance, then the balance is computed from the recorded ledger entries.
- Given a wallet transaction is unsuccessful and does not change the balance, when the system processes the failed transaction, then the system does not record a successful balance change for that transaction.

## FR-6: Manage Billers and Services

**Priority:** Must

**User Story:**

As an administrator, I want to add, edit, and disable billers and their services so that I can manage the payment services available through PayLink.

**Acceptance Criteria:**

- Given an administrator has permission to manage billers, when they submit the required information for a new biller or service, then the system adds it to the biller catalog.
- Given an existing biller or service is registered in the system, when the administrator edits its information, then the system saves the updated information.
- Given an existing biller or service is active, when the administrator disables it, then the system marks it as disabled.

## FR-7: View Billers and Required Input Fields

**Priority:** Must

**User Story:**

As a customer, I want to view the available billers and the information required by each service so that I know what details to provide before making a payment.

**Acceptance Criteria:**

- Given a customer opens the bill payment section, when the system retrieves the biller catalog, then it displays the available active billers and services.
- Given a customer selects a specific biller service, when the service details are displayed, then the system shows the required input fields for that service, such as a meter number or phone number.
- Given a biller or service has been disabled, when a customer views the available services, then the disabled service is not available for selection.

## FR-8: Bill Inquiry and Fee Calculation

**Priority:** Must

**User Story:**

As a customer, I want to perform a bill inquiry and see the bill amount, service fee, and total amount before paying so that I know exactly how much will be deducted from my wallet.

**Acceptance Criteria:**

- Given a customer selects an active biller service and enters the required information, when they submit a valid bill inquiry, then the system requests the bill information from the selected biller.
- Given the biller returns a valid bill amount, when the inquiry is completed, then the system displays the bill amount, applicable service fee, and total amount.
- Given the biller cannot return valid bill information, when the customer performs the inquiry, then the system displays an appropriate error or failure message.

## FR-9: Pay a Bill Using the Wallet

**Priority:** Must

**User Story:**

As a customer, I want to pay a bill using my PayLink wallet so that I can complete bill payments without using traditional payment channels.

**Acceptance Criteria:**

- Given a customer has completed a bill inquiry and has sufficient available wallet balance, when they confirm the payment, then the system starts processing the bill payment using their wallet.
- Given a customer does not have sufficient available wallet balance to cover the total amount, when they attempt to pay the bill, then the system rejects the payment and informs the customer that their balance is insufficient.
- Given a customer submits a valid bill payment request, when the payment is successfully confirmed by the biller, then the system records the payment as completed.

## FR-10: Idempotent Payment Requests

**Priority:** Must

**User Story:**

As a customer, I want a repeated payment request to return the original result so that I am never charged twice when my network is slow or the app resends the request.

**Acceptance Criteria:**

- Given a customer has submitted a payment request with an idempotency key, when the same request is submitted again with the same idempotency key, then the system does not create a new payment and returns the result of the original payment.
- Given a customer submits a payment request with a new idempotency key, when the request is valid, then the system processes it as a new payment.
- Given a payment request is submitted without an idempotency key, when the system validates the request, then the system rejects the request and displays an appropriate error message.

## FR-11: Payment Life Cycle

**Priority:** Must

**User Story:**

As a system administrator, I want every payment to follow a defined life cycle so that each payment is always in exactly one valid state.

**Acceptance Criteria:**

- Given a new payment is created, when the system registers it, then the payment starts in the Initiated state.
- Given a payment is in a specific state, when an event occurs that is allowed by the life cycle, for example, the biller confirms a payment in the SentToBiller state, then the system moves the payment to the corresponding next state (Completed).
- Given a payment is in a specific state, when an event occurs that is not an allowed transition, for example, moving from Completed to Failed, then the system rejects the transition and the payment state remains unchanged.
- Given a payment is in a final state (Completed, Rejected or Refunded), when any further event is received for the payment, then the system does not change the payment state.

## FR-12: Hold and Release Funds

**Priority:** Must

**User Story:**

As a customer, I want my money to be held before the biller is called and released if the payment fails so that my funds are protected during payment processing.

**Acceptance Criteria:**

- Given a payment passes the fraud checks and the wallet has sufficient available balance, when the system prepares to call the biller, then the system moves the total amount from the available balance to the held balance before sending the request to the biller.
- Given a payment is in the Failed state, when the system processes the failure, then the system releases the held amount back to the customer's available balance and moves the payment to Refunded.
- Given a payment is completed successfully, when the biller confirms the payment, then the system converts the held amount into a final charge.
- Given a payment is in the Unknown state, when the system has not yet confirmed that the biller did not receive the payment, then the system keeps the amount held and does not refund it automatically.

## FR-13: Payment Timeout and Retry

**Priority:** Must

**User Story:**

As a customer, I want a payment that times out to be handled safely so that I am not charged for a payment that the biller never received, and I am not left without a result.

**Acceptance Criteria:**

- Given a payment has been sent to a live biller, when the biller does not answer within the configured timeout (10 seconds), then the system moves the payment to Unknown, keeps the money held, and informs the customer that the payment is being processed.
- Given a payment is in the Unknown state, when the retry schedule is reached (after 1, 5 and 15 minutes), then the system re-queries the biller for the payment status.
- Given the biller confirms or refuses the payment during a retry, when the system receives the answer, then the system moves the payment to Completed or Failed accordingly.
- Given the system has completed all retries and the status is still unknown, when the retries are exhausted, then the payment remains in Unknown and waits for reconciliation.

## FR-14: Asynchronous Callbacks (TopUpNet)

**Priority:** Must

**User Story:**

As a system administrator, I want the system to accept asynchronous callbacks from TopUpNet and ignore duplicates so that mobile top-up payments are completed exactly once.

**Acceptance Criteria:**

- Given a mobile top-up payment was accepted by TopUpNet, when TopUpNet sends a callback with a "success" result, then the system completes the payment and records the result.
- Given TopUpNet sends a callback with a "failed" result, when the system receives the callback, then the system moves the payment to Failed and releases the held funds.
- Given a callback for a payment has already been processed, when TopUpNet sends the same callback again, then the system ignores the duplicate, does not change the payment, and logs the duplicate callback.
- Given a callback refers to a payment reference that does not exist, when the system receives the callback, then the system rejects the callback and logs the event.

## FR-15: Multiple Biller Integrations

**Priority:** Must

**User Story:**

As a customer, I want to pay bills for different billers that use different formats so that I can pay electricity, water and mobile top-up bills from one application.

**Acceptance Criteria:**

- Given a customer pays an electricity bill, when the system communicates with ElectroCo, then the system uses the ElectroCo REST/JSON integration and returns the result in the standard PayLink format.
- Given a customer pays a water bill, when the system communicates with AquaCo, then the system uses the AquaCo SOAP-style XML integration and returns the result in the standard PayLink format.
- Given a customer pays a mobile top-up, when the system communicates with TopUpNet, then the system uses the TopUpNet asynchronous REST/JSON integration and returns the result in the standard PayLink format.
- Given one biller is unavailable, when customers pay bills for other billers, then those payments continue to be processed normally.

## FR-16: Fee Calculation Rules

**Priority:** Must

**User Story:**

As a customer, I want the service fee to be calculated correctly according to the biller type so that I know exactly how much I will pay.

**Acceptance Criteria:**

- Given a customer pays an electricity or water bill, when the system calculates the fee, then the system applies a fixed fee of 2.50 EGP.
- Given a customer pays a mobile top-up, when the system calculates the fee, then the system applies 1.5% of the amount with a minimum fee of 1 EGP.
- Given a customer pays an internet bill, when the system calculates the fee, then the system applies 2 EGP for amounts up to 200 EGP and 4 EGP for amounts above 200 EGP.
- Given a promotion is active for a selected biller within the configured start and end dates, when the system calculates the fee for that biller, then the system applies a fee of 0.
- Given the promotion period has ended or has not started, when the system calculates the fee, then the system applies the normal fee rule.

## FR-17: Agent Payments and Commission

**Priority:** Should

**User Story:**

As an agent, I want to pay a bill on behalf of a customer and earn a commission so that I am rewarded for serving customers at my terminal.

**Acceptance Criteria:**

- Given an authorized agent initiates a payment on behalf of a customer, when the payment is submitted with valid information, then the system processes the payment and records the agent as the payment channel.
- Given a payment made through an agent is completed, when the system finalizes the payment, then the system credits the agent's wallet with a commission of 40% of the service fee.
- Given a payment made through an agent fails or is refunded, when the system processes the failure, then the system does not credit any commission to the agent.
- Given a payment is made directly by a customer without an agent, when the payment is completed, then the system does not record any agent commission.

## FR-18: Payment Limits Validation

**Priority:** Must

**User Story:**

As a customer, I want payments above the allowed limits to be rejected with a clear reason so that I understand why my payment was not accepted.

**Acceptance Criteria:**

- Given a customer submits a payment below 5 EGP or above 10,000 EGP, when the system validates the payment, then the system rejects the payment and displays a message explaining the single-payment limit.
- Given a customer has a Basic account and the payment would exceed the daily limit of 5,000 EGP, when the system validates the payment, then the system rejects the payment and displays a message explaining the daily limit.
- Given a customer has a Verified account and the payment would exceed the daily limit of 30,000 EGP, when the system validates the payment, then the system rejects the payment and displays a message explaining the daily limit.
- Given a payment is rejected because of a limit, when the system processes the rejection, then the payment moves to the Rejected state and no funds are held.

## FR-19: Velocity Blocking

**Priority:** Should

**User Story:**

As a customer, I want excessive payment attempts to temporarily block my account so that suspicious activity is limited.

**Acceptance Criteria:**

- Given an account has made 5 payment attempts within 60 seconds, when it submits another payment attempt within that window, then the system blocks the account for 10 minutes.
- Given an account is velocity-blocked, when it attempts a payment during the 10-minute block, then the system rejects the attempt and provides a clear reason.
- Given the 10-minute block has expired, when the customer attempts a payment, then the system allows the request to continue through normal validation.

## FR-20: Payment Search and History

**Priority:** Must

**User Story:**

As a support employee, I want to search for a payment by reference and view its full history so that I can investigate customer issues.

**Acceptance Criteria:**

- Given a support employee has the required access, when they search using a valid payment reference, then the system displays the payment details and its recorded history.
- Given a support employee searches for an unknown reference, when the search is submitted, then the system indicates that no matching payment was found.
- Given a payment has multiple events or status changes, when its history is opened, then the system displays those events in chronological order.

## FR-21: Block and Unblock Account

**Priority:** Should

**User Story:**

As a support employee, I want to block and unblock a customer account so that I can manage account restrictions when needed.

**Acceptance Criteria:**

- Given an authorized support employee selects an active account, when they block it, then the system marks the account as blocked and prevents payment attempts.
- Given an account is blocked, when an authorized employee unblocks it, then the system restores the account to an unblocked status.
- Given an employee without permission attempts to block or unblock an account, when the action is submitted, then the system rejects it.

## FR-22: Customer Notifications

**Priority:** Must

**User Story:**

As a customer, I want to receive SMS and push notifications when a payment completes or fails so that I know its outcome.

**Acceptance Criteria:**

- Given a payment reaches Completed, when the final status is recorded, then the system attempts to send SMS and push notifications.
- Given a payment reaches Failed, when the final status is recorded, then the system attempts to send SMS and push notifications.
- Given a payment is in Unknown, when no final outcome has been confirmed, then the system does not send a definitive success or failure notification.

## FR-23: Notification Retry

**Priority:** Should

**User Story:**

As the system, I want failed notifications to be retried and eventually marked undelivered so that notification failures are tracked.

**Acceptance Criteria:**

- Given an SMS or push notification attempt fails, when the retry policy is executed, then the system retries the failed notification up to 3 additional times.
- Given all retry attempts fail, when the retry limit is reached, then the notification is marked Undelivered.
- Given a notification is delivered successfully, when a later retry is scheduled, then the system does not send unnecessary additional attempts.

## FR-24: Admin Fee and Limit Configuration

**Priority:** Should

**User Story:**

As an administrator, I want to edit fee and limit values without redeploying the application so that business settings can be updated easily.

**Acceptance Criteria:**

- Given an authorized administrator enters valid fee or limit values, when they save the configuration, then the system stores the updated values without requiring a redeployment.
- Given an administrator enters invalid values, when they attempt to save, then the system rejects the configuration and explains the validation error.
- Given updated configuration values are saved, when a new payment is initiated, then the system uses the updated values according to the agreed configuration rules.

## FR-25: Audit Log

**Priority:** Must

**User Story:**

As an administrator, I want every money movement and administrative action recorded in an audit log so that actions can be traced and reviewed.

**Acceptance Criteria:**

- Given a wallet money movement or administrative action occurs, when the action is processed, then the system records an audit entry containing the actor or system identity, action, timestamp, affected entity, and reference.
- Given an audit entry has been recorded, when an authorized reviewer retrieves it, then the entry is available for review.
- Given an audit entry exists, when an ordinary user attempts to modify or delete it, then the system prevents silent alteration or deletion.

## FR-26: Daily Reconciliation Report

**Priority:** Should

**User Story:**

As an administrator, I want a daily reconciliation report generated from a settlement file so that I can identify differences between biller settlements and PayLink records.

**Acceptance Criteria:**

- Given a valid settlement file is provided, when the reconciliation process runs, then the system compares settlement entries with PayLink payment records.
- Given a settlement entry does not match a PayLink record, when the comparison is completed, then the report flags the mismatch for investigation.
- Given reconciliation completes, when an administrator views the report, then the report shows the reconciliation results and mismatches.

## FR-27: Refund Request for Completed Payment

**Priority:** Could

**User Story:**

As a customer, I want to request a refund for a completed payment so that support can review my request.

**Acceptance Criteria:**

- Given a customer has a completed payment, when they submit a refund request, then the system records the request linked to that payment.
- Given a refund request is pending, when authorized support approves or rejects it, then the system records the decision and its outcome.
- Given a refund request is rejected, when the decision is recorded, then the payment is not refunded through that request.

## FR-28: Daily Admin Statistics

**Priority:** Could

**User Story:**

As an administrator, I want to view daily payment totals, fees, commissions, and failures per biller so that I can monitor operations.

**Acceptance Criteria:**

- Given an administrator selects a day, when they view the daily statistics, then the system displays payment totals, fees earned, commissions paid, and failures per biller.
- Given payments belong to different billers, when the statistics are calculated, then the results are grouped by biller.
- Given no transactions exist for a biller on the selected day, when the report is displayed, then the biller appears with zero totals or is clearly indicated as having no transactions.

# 3. Non-Functional Requirements

## NFR-1: Correctness

**Priority:** Must

**Description:**

The PayLink system must process financial transactions accurately and maintain correct wallet balances. It must prevent duplicate charges and ensure that a customer's wallet balance never becomes negative, even when multiple payment requests arrive simultaneously.

**Measurable Targets:**

- Zero double charges in duplicate payment tests.
- Zero negative wallet balances in concurrent payment tests.

**Verification Method:**

The system will be tested by sending the same payment request multiple times and by sending two payment requests simultaneously from a wallet that has enough funds for only one payment. The expected result is that only one payment succeeds, no duplicate charge occurs, and the wallet balance never becomes negative.

## NFR-2: Performance

**Priority:** Must

**Description:**

The PayLink system must process payment requests efficiently and maintain stable performance under load. It should be capable of handling a large number of payment requests within a short period without becoming unavailable.

**Measurable Target:**

- The system must sustain 100 payments per second for 1 minute against the mock billers.

**Verification Method:**

A load test will send payment requests to the system at a rate of 100 payments per second for one continuous minute using the mock billers. The system must sustain this rate throughout the test.

## NFR-3: Resilience

**Priority:** Must

**Description:**

The PayLink system must keep working when one biller fails. A biller outage, a very slow response or an error must only affect payments to that biller, and payments to all other billers must continue to be processed normally.

Payments to the failing biller must still follow the payment life cycle: a timeout moves the payment to Unknown and keeps the money held, and a refusal moves it to Failed and releases the hold.

**Measurable Targets:**

- When one biller is unavailable, at least 99% of payments to the other billers still complete successfully.
- Payments to the unavailable biller are never left without a state. After 10 seconds each one is in Unknown, Failed or Refunded, and no payment is lost.
- The average response time of payments to healthy billers does not increase because of the outage.

**Verification Method:**

A load test will send payments to all three mock billers (ElectroCo, AquaCo and TopUpNet) while one mock biller, for example AquaCo, is switched off or made to answer after 12 seconds.

The test will measure the success rate of payments to the other two billers, and it will check that every payment to the failing biller ends in a valid state with its funds held or released correctly. The result will be reported in the pipeline test output.

## NFR-4: Modifiability

**Priority:** Must

**Description:**

The PayLink system must be easy to extend with new billers and to adapt when a biller changes its API.

Each biller has its own adapter that hides its protocol, so adding a biller or changing a biller's integration must not require changes to the other modules, such as Payment Processing, Accounts and Wallet, Fees and Commissions, or Notifications.

**Measurable Targets:**

- Adding a new biller requires changes only in the Biller Integration module and configuration, which means 0 modified files in any other module.
- The ElectroCo API v2 change (new field names, piasters and signed requests) requires changes only in the ElectroCo adapter, which means 0 modified files in the other modules.

**Verification Method:**

A new mock biller will be added to the system in a single commit, and the list of changed files in that commit (`git diff`) will be checked.

Every changed file must be inside the Biller Integration module or the configuration files.

The same check will be repeated for the commit that applies the ElectroCo v2 change. The results will be included in the final report.

## NFR-5: Auditability

**Priority:** Must

**Description:**

PayLink must maintain traceable records for every money movement and administrative action.

Audit records must capture who or what performed the action, what action occurred, when it occurred, the affected entity, and its reference. Records must be retrievable for review and must not be silently altered.

**Measurable Targets:**

- 100% of money-movement and administrative-action scenarios in the automated tests produce an audit record with the required fields.
- Audit records can be retrieved by transaction or entity reference during verification.

**Verification Method:**

Automated tests will exercise wallet movements and administrative actions, validate required audit fields, and verify retrieval by reference.

## NFR-6: Testability

**Priority:** Must

**Description:**

PayLink must be designed so that functional requirements can be verified through automated tests.

Core business logic must be testable independently from external biller, notification, and other third-party integrations.

**Measurable Targets:**

- Every FR feature has at least one automated test for its principal behavior and relevant failure path.
- External services can be replaced with mocks or test doubles during tests.
- The test suite can be run using one documented command.
- Target core-logic test coverage: at least 90%, subject to team agreement.

**Verification Method:**

The automated test suite will cover assigned requirements, use mocks for external dependencies, and report coverage for core logic.

# 4. Ambiguities and Team Decisions

This section identifies unclear or unspecified details in functional requirements FR-1 to FR-28 and records the team's decisions to ensure consistent system behaviour during development.

## 4.1 FR-1: Customer Registration

**Ambiguity 1:** What information is required to register a new customer?

**Decision:** Customers must provide their full name, phone number, and password during registration.

**Ambiguity 2:** Can multiple accounts use the same phone number?

**Decision:** Each phone number must be unique and associated with only one customer account.

**Ambiguity 3:** Does a customer need to verify their phone number during registration?

**Decision:** The customer must verify their phone number using an OTP before the account becomes active.

## 4.2 FR-2: Upgrade to Verified Account

**Ambiguity 1:** What is required for a customer to upgrade from Basic to Verified?

**Decision:** The customer must submit the required identity information to request verification.

**Ambiguity 2:** Who approves the verification request?

**Decision:** An authorized administrator reviews the submitted information and approves or rejects the request.

**Ambiguity 3:** What happens to the customer's daily payment limit after verification?

**Decision:** The daily payment limit increases from 5,000 EGP for Basic accounts to 30,000 EGP for Verified accounts, as specified in the project brief.

## 4.3 FR-3: View Wallet Balance and Transaction History

**Ambiguity 1:** Should available and held balances be displayed separately?

**Decision:** Yes. The system must display the available balance and held balance separately.

**Ambiguity 2:** What information should appear in the transaction history?

**Decision:** Each transaction should display its reference, amount, date, transaction type, and status.

**Ambiguity 3:** Can customers view the wallet history of other customers?

**Decision:** No. Each customer can only access their own wallet balance and transaction history.

## 4.4 FR-4: Wallet Top-Up

**Ambiguity 1:** Which methods are supported for adding money to a wallet?

**Decision:** The system supports simulated card payments and cash top-ups through authorized agents.

**Ambiguity 2:** When should the wallet balance be increased?

**Decision:** The wallet balance is increased only after the top-up operation is successfully confirmed.

**Ambiguity 3:** What happens if a top-up operation fails?

**Decision:** The system must not increase the customer's wallet balance when a top-up fails.

## 4.5 FR-5: Wallet Ledger

**Ambiguity 1:** Can the system update the wallet balance directly?

**Decision:** No. Wallet balances must be calculated from ledger entries rather than being overwritten directly.

**Ambiguity 2:** What information should each ledger entry contain?

**Decision:** Each ledger entry should include the transaction reference, amount, entry type, timestamp, and associated wallet.

**Ambiguity 3:** Can existing ledger entries be modified or deleted?

**Decision:** No. Ledger entries must remain immutable to preserve accurate financial records.

## 4.6 FR-6: Manage Billers and Services

**Ambiguity 1:** Who is allowed to add, edit, or disable billers?

**Decision:** Only authorized administrators can manage billers and their services.

**Ambiguity 2:** What happens when a biller or service is disabled?

**Decision:** Customers cannot initiate new payments through a disabled biller or service.

**Ambiguity 3:** Can a disabled biller or service be activated again?

**Decision:** Yes. An authorized administrator can reactivate a previously disabled biller or service.

## 4.7 FR-7: View Billers and Required Input Fields

**Ambiguity 1:** Should disabled billers and services appear in the customer's available list?

**Decision:** No. Only active billers and services should be displayed to customers.

**Ambiguity 2:** Are the required input fields the same for every biller?

**Decision:** No. Each biller service defines its own required input fields, such as a meter number or phone number.

**Ambiguity 3:** What happens if a customer does not provide all required information?

**Decision:** The system displays a validation message and does not proceed with the inquiry until all required fields are provided.

## 4.8 FR-8: Bill Inquiry and Fee Calculation

**Ambiguity 1:** Should the customer see the service fee before confirming payment?

**Decision:** Yes. The system must display the bill amount, applicable service fee, and total amount before payment confirmation.

**Ambiguity 2:** What happens if the biller does not respond to an inquiry?

**Decision:** The inquiry is treated as unsuccessful, and the system displays an appropriate error message. No payment is initiated.

**Ambiguity 3:** Can a customer use an old bill inquiry result to make a payment?

**Decision:** The customer must use a valid inquiry result that has not expired. The validity period must be agreed upon by the team.

## 4.9 FR-9: Pay a Bill Using the Wallet

**Ambiguity 1:** When should the customer's funds be deducted from the available balance?

**Decision:** The system must hold the required funds before sending the payment request to the biller. The funds are not considered finally spent until the payment is confirmed.

**Ambiguity 2:** What happens if the customer's available balance is insufficient?

**Decision:** The system rejects the payment and displays an insufficient-balance message.

**Ambiguity 3:** What happens if the biller does not respond within the specified timeout?

**Decision:** The payment moves to the Unknown state, and the held funds remain reserved until the system confirms whether the biller received the payment.

## 4.10 FR-10: Idempotent Payment Requests

**Ambiguity 1:** Who generates the idempotency key, the client or the server?

**Decision:** The client app generates a unique key (for example, a UUID) and sends it with every payment request.

**Ambiguity 2:** How long is an idempotency key remembered?

**Decision:** Keys are stored for 24 hours. After that period, the same key may be treated as a new request.

**Ambiguity 3:** What happens if the same idempotency key is sent with different payment details?

**Decision:** The system rejects the request with a conflict error and does not process it.

## 4.11 FR-11: Payment Life Cycle

**Ambiguity 1:** Can a payment skip states or move backwards in the life cycle?

**Decision:** No. Only the transitions defined in section 2.5 of the project brief are allowed. Any other transition is rejected and the payment state remains unchanged.

**Ambiguity 2:** Which states are final?

**Decision:** Completed, Rejected, and Refunded are final states. No further changes are allowed once a payment reaches one of them.

**Ambiguity 3:** Is the Failed state final?

**Decision:** No. Failed is a temporary state. Once the hold is released to the wallet, the payment moves to Refunded.

## 4.12 FR-12: Hold and Release Funds

**Ambiguity 1:** When exactly are the funds held?

**Decision:** Funds are held only after the fraud checks and balance check pass, and before the request is sent to the biller.

**Ambiguity 2:** Is the hold released when a payment is rejected?

**Decision:** No hold is needed. A Rejected payment never has a hold because funds are only held after all checks pass.

**Ambiguity 3:** Can funds in an Unknown payment be refunded automatically?

**Decision:** No. Funds stay held until the system is sure the biller did not receive the payment, through a retry, a callback, or reconciliation.

## 4.13 FR-13: Payment Timeout and Retry

**Ambiguity 1:** What does the customer see while a payment is Unknown?

**Decision:** The customer sees a "payment is being processed" message, the money stays held, and the final result is sent by notification once known.

**Ambiguity 2:** When are the retries performed?

**Decision:** The system re-queries the biller 3 times, after 1, 5, and 15 minutes. These values are stored in configuration.

**Ambiguity 3:** What happens if the biller still does not answer after all retries?

**Decision:** The payment remains Unknown with the money held until reconciliation or a later biller confirmation resolves it. It is never refunded automatically.

## 4.14 FR-14: Asynchronous Callbacks (TopUpNet)

**Ambiguity 1:** How does the system verify that a callback is genuine?

**Decision:** The callback must contain a known payment reference. Callbacks with an unknown reference are rejected and logged. Signature validation is an optional improvement.

**Ambiguity 2:** How are duplicate callbacks detected?

**Decision:** If the payment has already reached a final result, the duplicate callback is ignored, the payment is not changed, and the event is logged.

**Ambiguity 3:** What happens if TopUpNet never sends the callback?

**Decision:** The payment stays in Unknown after the retry schedule and is resolved through reconciliation.

## 4.15 FR-15: Multiple Biller Integrations

**Ambiguity 1:** Is NetCo (batch CSV) required?

**Decision:** No. NetCo is optional. The minimum is ElectroCo, AquaCo, and TopUpNet. NetCo is added only if time allows.

**Ambiguity 2:** How does the system handle the different formats of each biller?

**Decision:** Each biller has its own adapter that converts its protocol and error codes into one standard PayLink format used by the rest of the system.

**Ambiguity 3:** What happens to other billers when one biller is down?

**Decision:** Payments to other billers continue normally. Only payments to the unavailable biller are affected.

## 4.16 FR-16: Fee Calculation Rules

**Ambiguity 1:** Is the promotion checked before or after the normal fee rule?

**Decision:** The promotion is checked first. If it is active for the selected biller within its start and end dates, the fee is 0.

**Ambiguity 2:** Which fee applies to an internet bill of exactly 200 EGP?

**Decision:** The 2 EGP fee applies, because the rule says "up to 200 EGP".

**Ambiguity 3:** How is the percentage fee rounded?

**Decision:** Fees use exact decimal types and are rounded to 2 decimal places (half-up). Floating point is never used.

## 4.17 FR-17: Agent Payments and Commission

**Ambiguity 1:** Who pays the service fee and the commission when an agent pays on behalf of a customer?

**Decision:** The customer's wallet is charged the amount and the fee. The commission (40% of the fee) is taken from PayLink's fee income and credited to the agent's wallet.

**Ambiguity 2:** When is the commission credited?

**Decision:** Only when the payment reaches the Completed state. No commission is paid for Failed, Rejected, Unknown, or Refunded payments.

**Ambiguity 3:** Is commission paid when a promotion makes the fee 0?

**Decision:** No. The commission is 40% of the fee, so it is 0 when the fee is 0.

## 4.18 FR-18: Payment Limits Validation

**Ambiguity 1:** Does the daily limit count only completed payments?

**Decision:** The daily limit counts completed payments plus payments in progress (held funds or Unknown). Failed, Rejected, and Refunded payments are not counted.

**Ambiguity 2:** Are the minimum and maximum single-payment limits applied to the bill amount or the total including the fee?

**Decision:** The 5 EGP minimum and 10,000 EGP maximum apply to the bill amount. The daily limit is checked against the total amount including the fee.

**Ambiguity 3:** When does the daily limit reset?

**Decision:** The daily limit resets at midnight (00:00) Egypt local time (Africa/Cairo), and this value is stored in configuration.

## 4.19 FR-19: Velocity Blocking

**Ambiguity 1:** Does "more than 5 payments in 60 seconds" mean the 6th attempt triggers the block?

**Decision:** Treat the rule as a rolling 60-second window; the 6th attempt triggers the 10-minute block.

**Ambiguity 2:** Does the block prevent all payment attempts?

**Decision:** Reject payment attempts while the velocity block is active and return a clear reason.

**Ambiguity 3:** Does the block expire automatically?

**Decision:** The velocity block expires after 10 minutes unless another restriction applies.

## 4.20 FR-20: Payment Search and History

**Ambiguity 1:** What information is included in the payment history?

**Decision:** Include payment reference, amount, timestamps, status changes, and related recorded events, subject to support permissions.

**Ambiguity 2:** Can support search only by reference?

**Decision:** Phase 1 acceptance is reference-based search as specified; additional search filters can be considered later.

**Ambiguity 3:** Who can access full payment history?

**Decision:** Only authorized support users can access it, with access recorded where applicable.

## 4.21 FR-21: Block and Unblock Account

**Ambiguity 1:** Is an administrative block separate from the velocity block?

**Decision:** Track administrative account blocking separately from automatic velocity blocking.

**Ambiguity 2:** Who can block or unblock accounts?

**Decision:** Only authorized support employees with the appropriate permission.

**Ambiguity 3:** Is a reason required?

**Decision:** Require a reason for manual block/unblock actions and record it in the audit log.

## 4.22 FR-22: Customer Notifications

**Ambiguity 1:** Are SMS and push channels independent?

**Decision:** Attempt each channel independently so a failure in one does not prevent the other.

**Ambiguity 2:** What statuses trigger notifications?

**Decision:** Send outcome notifications only for Completed and Failed statuses; Unknown is not a final outcome.

**Ambiguity 3:** What information is included?

**Decision:** Include payment reference, outcome, and concise details without exposing sensitive information.

## 4.23 FR-23: Notification Retry

**Ambiguity 1:** Does "retry 3 times" include the first attempt?

**Decision:** Interpret as 3 additional retries after the initial failed attempt.

**Ambiguity 2:** What retry timing is used?

**Decision:** Retry timing should be configurable or agreed by the team; no specific interval is prescribed in the brief.

**Ambiguity 3:** How is final failure represented?

**Decision:** Mark the notification Undelivered after all attempts fail and retain the delivery-attempt history.

## 4.24 FR-24: Admin Fee and Limit Configuration

**Ambiguity 1:** When do new values take effect?

**Decision:** Apply saved values to new payments; existing payments retain the values captured when initiated.

**Ambiguity 2:** What values are valid?

**Decision:** Validate fees and limits as non-negative, within agreed business ranges, and internally consistent.

**Ambiguity 3:** Are changes audited?

**Decision:** Record the administrator, old value, new value, and timestamp in the audit log.

## 4.25 FR-25: Audit Log

**Ambiguity 1:** Which fields must be stored?

**Decision:** Store actor/system identity, action, timestamp, affected entity, transaction/reference ID, and relevant outcome.

**Ambiguity 2:** Can records be changed?

**Decision:** Audit records are append-only for normal application access; corrections are recorded as new events.

**Ambiguity 3:** How long are logs retained?

**Decision:** Retention duration must be agreed by the team; Phase 1 will document the selected retention policy.

## 4.26 FR-26: Daily Reconciliation Report

**Ambiguity 1:** What happens to malformed settlement files?

**Decision:** Reject the file with validation details and do not produce misleading reconciliation results.

**Ambiguity 2:** How are duplicate settlement rows handled?

**Decision:** Detect duplicate entries and flag them rather than silently counting them twice.

**Ambiguity 3:** Which day and time zone define "daily"?

**Decision:** Use Egypt local time (Africa/Cairo) unless the team agrees otherwise.

## 4.27 FR-27: Refund Request for Completed Payment

**Ambiguity 1:** Are refunds full or partial?

**Decision:** Phase 1 supports full-payment refund requests only; partial refunds are out of scope unless the team approves them.

**Ambiguity 2:** Can multiple requests be created for one payment?

**Decision:** Allow only one active refund request per payment to prevent duplicate processing.

**Ambiguity 3:** What happens after approval?

**Decision:** Approval initiates the refund process; the payment and wallet records must be updated once, and the outcome audited.

## 4.28 FR-28: Daily Admin Statistics

**Ambiguity 1:** Which time zone defines a day?

**Decision:** Use Egypt local time (Africa/Cairo) for daily aggregation.

**Ambiguity 2:** What counts as a payment total?

**Decision:** Team must define whether totals count initiated, completed, and/or failed transactions; recommended separate counts by status.

**Ambiguity 3:** How are fees and commissions calculated in the report?

**Decision:** Use recorded transaction fee and commission values, not recalculation from current settings.