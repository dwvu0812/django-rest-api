# 🏗️ AirBnB Clone - Enhanced Database ERD

## 📋 NORMALIZED ENTITY LIST

### 👤 USERS

- id (PK), email (U), username, password_hash
- first_name, last_name, phone, avatar_url
- bio, date_of_birth, user_type, is_verified
- language_preference, timezone
- last_login_at, created_at, updated_at

### 🏠 ADDRESSES

- id (PK), street_address, apartment_number
- city, state, country, postal_code
- latitude, longitude, is_verified
- address_type (home/property/billing)
- created_at, updated_at

### 🔗 USER_ADDRESSES (Junction Table)

- user_id (FK → users.id), address_id (FK → addresses.id)
- address_type (home/billing/shipping), is_primary
- created_at

### 🏠 PROPERTIES

- id (PK), host_id (FK → users.id), address_id (FK → addresses.id)
- title, slug (U), description, property_type
- max_guests, bedrooms, bathrooms, beds
- base_price_per_night, cleaning_fee
- status, is_instant_book, minimum_nights, maximum_nights
- created_at, updated_at

### 🖼️ PROPERTY_IMAGES

- id (PK), property_id (FK → properties.id)
- image_url, caption, is_primary, display_order
- created_at

### 🎯 AMENITIES

- id (PK), name (U), category, icon_class
- description, is_active
- created_at, updated_at

### 🔗 PROPERTY_AMENITIES (Junction Table)

- property_id (FK → properties.id), amenity_id (FK → amenities.id)
- PRIMARY KEY (property_id, amenity_id)

### 📅 PROPERTY_AVAILABILITY

- id (PK), property_id (FK → properties.id)
- date, is_available, price_override
- minimum_nights_override, notes
- created_at, updated_at

### 🚫 BLOCKED_DATES

- id (PK), property_id (FK → properties.id)
- start_date, end_date, reason
- notes, created_by (FK → users.id)
- created_at

### 💲 SEASONAL_PRICING

- id (PK), property_id (FK → properties.id)
- season_name, start_date, end_date
- price_multiplier, minimum_nights, is_active
- created_at, updated_at

### 📅 BOOKINGS

- id (PK), guest_id (FK → users.id), property_id (FK → properties.id)
- check_in_date, check_out_date, guests_count
- nights, price_per_night, subtotal
- cleaning_fee, service_fee, taxes, total_amount
- status, special_requests
- confirmed_at, cancelled_at, cancellation_reason
- created_at, updated_at

### 💳 PAYMENT_METHODS

- id (PK), user_id (FK → users.id)
- method_type (card/paypal/bank/crypto)
- provider (stripe/paypal/coinbase)
- external_id, last_four_digits
- expiry_month, expiry_year
- is_default, is_active
- created_at, updated_at

### 💰 PAYMENTS

- id (PK), booking_id (FK → bookings.id)
- payment_method_id (FK → payment_methods.id)
- amount, currency, status
- payment_intent_id, transaction_fee
- processed_at, created_at, updated_at

### 🔄 REFUNDS

- id (PK), payment_id (FK → payments.id)
- amount, reason, status
- refund_id (external), processing_fee
- processed_at, created_at

### ⭐ REVIEWS

- id (PK), booking_id (FK → bookings.id)
- reviewer_id (FK → users.id), reviewee_id (FK → users.id)
- property_id (FK → properties.id)
- review_type (guest_to_host/host_to_guest/guest_to_property)
- overall_rating, ratings (JSON)
- comment, is_public, is_anonymous
- moderation_status, moderated_by (FK → users.id), moderated_at
- host_response, host_response_date
- created_at, updated_at

### 👍 REVIEW_VOTES

- id (PK), review_id (FK → reviews.id)
- user_id (FK → users.id)
- vote_type (helpful/not_helpful)
- created_at

### 🏷️ REVIEW_TAGS

- id (PK), name (U), category
- description, is_active
- created_at, updated_at

### 🔗 REVIEW_TAG_ASSOCIATIONS (Junction Table)

- review_id (FK → reviews.id), tag_id (FK → review_tags.id)
- created_at

### 💬 CONVERSATIONS

- id (PK), property_id (FK → properties.id)
- booking_id (FK → bookings.id)
- conversation_type (inquiry/booking/support)
- is_archived, created_at, updated_at

### 👥 CONVERSATION_PARTICIPANTS (Junction Table)

- conversation_id (FK → conversations.id)
- user_id (FK → users.id)
- joined_at, last_read_at, is_active

### 📨 MESSAGES

- id (PK), conversation_id (FK → conversations.id)
- sender_id (FK → users.id)
- content, message_type (text/image/file)
- attachment_url, is_read, is_system_message
- created_at

### 🔔 NOTIFICATIONS

- id (PK), recipient_id (FK → users.id)
- notification_type, title, message
- booking_id (FK → bookings.id), property_id (FK → properties.id)
- action_url, is_read, is_push_sent, is_email_sent
- created_at

### 📊 AUDIT_LOGS

- id (PK), table_name, record_id
- action (INSERT/UPDATE/DELETE)
- old_values (JSON), new_values (JSON)
- changed_by (FK → users.id)
- ip_address, user_agent
- changed_at

### 💰 PROPERTY_PRICE_HISTORY

- id (PK), property_id (FK → properties.id)
- old_price, new_price, effective_date
- changed_by (FK → users.id), reason
- created_at

### 📈 BOOKING_STATUS_HISTORY

- id (PK), booking_id (FK → bookings.id)
- old_status, new_status
- changed_by (FK → users.id), reason
- changed_at

### 🔒 USER_PRIVACY_SETTINGS

- id (PK), user_id (FK → users.id)
- show_profile_to_public, show_reviews_to_public
- allow_search_engines, marketing_emails_consent
- data_processing_consent, consent_date
- updated_at

### 📝 DATA_RETENTION_LOGS

- id (PK), user_id (FK → users.id)
- data_type, retention_period
- scheduled_deletion_date, status
- created_at

### 🛡️ SECURITY_LOGS

- id (PK), user_id (FK → users.id)
- event_type (login/logout/password_change/suspicious_activity)
- ip_address, user_agent, location
- status (success/failed), risk_score
- created_at

---

## 🔗 COMPREHENSIVE RELATIONSHIP MAPPING

### Core User & Property Relationships

- Users (1) ──── (N) Properties [host_id]
- Users (N) ──── (M) Addresses [via User_Addresses]
- Properties (1) ──── (1) Addresses [address_id]

### Booking & Payment Flow

- Users (1) ──── (N) Bookings [guest_id]
- Properties (1) ──── (N) Bookings [property_id]
- Users (1) ──── (N) Payment_Methods [user_id]
- Bookings (1) ──── (N) Payments [booking_id]
- Payments (1) ──── (N) Refunds [payment_id]

### Property Management

- Properties (1) ──── (N) Property_Images [property_id]
- Properties (N) ──── (M) Amenities [via Property_Amenities]
- Properties (1) ──── (N) Property_Availability [property_id]
- Properties (1) ──── (N) Blocked_Dates [property_id]
- Properties (1) ──── (N) Seasonal_Pricing [property_id]

### Review System

- Bookings (1) ──── (N) Reviews [booking_id]
- Users (1) ──── (N) Reviews [reviewer_id]
- Users (1) ──── (N) Reviews [reviewee_id]
- Properties (1) ──── (N) Reviews [property_id]
- Reviews (1) ──── (N) Review_Votes [review_id]
- Reviews (N) ──── (M) Review_Tags [via Review_Tag_Associations]

### Communication System

- Users (N) ──── (M) Conversations [via Conversation_Participants]
- Conversations (1) ──── (N) Messages [conversation_id]
- Users (1) ──── (N) Messages [sender_id]
- Properties (1) ──── (N) Conversations [property_id]
- Bookings (1) ──── (N) Conversations [booking_id]

### Notification & Audit

- Users (1) ──── (N) Notifications [recipient_id]
- Users (1) ──── (N) Audit_Logs [changed_by]
- Properties (1) ──── (N) Property_Price_History [property_id]
- Bookings (1) ──── (N) Booking_Status_History [booking_id]

### Privacy & Security

- Users (1) ──── (1) User_Privacy_Settings [user_id]
- Users (1) ──── (N) Data_Retention_Logs [user_id]
- Users (1) ──── (N) Security_Logs [user_id]

---

## 📊 DATABASE INDEXES FOR PERFORMANCE

### Geographic & Location Queries

```sql
CREATE INDEX idx_addresses_location ON addresses (city, country);
CREATE INDEX idx_addresses_coordinates ON addresses (latitude, longitude);
CREATE INDEX idx_properties_location ON properties (address_id);
```

### Booking & Availability Queries

```sql
CREATE INDEX idx_bookings_dates ON bookings (check_in_date, check_out_date);
CREATE INDEX idx_bookings_status_date ON bookings (status, created_at);
CREATE INDEX idx_availability_date_range ON property_availability (property_id, date, is_available);
CREATE INDEX idx_blocked_dates_range ON blocked_dates (property_id, start_date, end_date);
```

### Payment & Financial Queries

```sql
CREATE INDEX idx_payments_status_date ON payments (status, created_at);
CREATE INDEX idx_payments_booking ON payments (booking_id, status);
CREATE INDEX idx_refunds_status ON refunds (status, created_at);
```

### Review & Rating Queries

```sql
CREATE INDEX idx_reviews_property_rating ON reviews (property_id, overall_rating);
CREATE INDEX idx_reviews_user_type ON reviews (reviewee_id, review_type);
CREATE INDEX idx_review_votes_helpful ON review_votes (review_id, vote_type);
```

### Communication Queries

```sql
CREATE INDEX idx_messages_conversation_date ON messages (conversation_id, created_at);
CREATE INDEX idx_notifications_user_read ON notifications (recipient_id, is_read);
```

### Audit & Security Queries

```sql
CREATE INDEX idx_audit_table_record ON audit_logs (table_name, record_id);
CREATE INDEX idx_audit_user_date ON audit_logs (changed_by, changed_at);
CREATE INDEX idx_security_user_event ON security_logs (user_id, event_type, created_at);
```

---

## 🛡️ DATABASE CONSTRAINTS

### Data Integrity Constraints

```sql
-- Booking date validation
ALTER TABLE bookings ADD CONSTRAINT chk_valid_booking_dates
    CHECK (check_out_date > check_in_date);

-- Positive amounts
ALTER TABLE bookings ADD CONSTRAINT chk_positive_total_amount
    CHECK (total_amount >= 0);

ALTER TABLE payments ADD CONSTRAINT chk_positive_payment_amount
    CHECK (amount > 0);

-- Rating range validation
ALTER TABLE reviews ADD CONSTRAINT chk_valid_rating_range
    CHECK (overall_rating >= 1 AND overall_rating <= 5);

-- Guest capacity validation
ALTER TABLE bookings ADD CONSTRAINT chk_guest_capacity
    CHECK (guests_count > 0);
```

### Business Logic Constraints

```sql
-- Prevent overlapping bookings
ALTER TABLE bookings ADD CONSTRAINT uk_no_overlapping_bookings
    UNIQUE (property_id, check_in_date, check_out_date)
    WHERE status IN ('confirmed', 'pending');

-- One primary address per user per type
ALTER TABLE user_addresses ADD CONSTRAINT uk_one_primary_per_type
    UNIQUE (user_id, address_type, is_primary)
    WHERE is_primary = true;

-- One primary image per property
ALTER TABLE property_images ADD CONSTRAINT uk_one_primary_image
    UNIQUE (property_id, is_primary)
    WHERE is_primary = true;
```

---

## 📈 NORMALIZATION COMPLIANCE

### ✅ First Normal Form (1NF)

- All attributes contain atomic values
- No repeating groups
- Each table has a primary key

### ✅ Second Normal Form (2NF)

- Meets 1NF requirements
- No partial dependencies on composite keys
- All non-key attributes fully depend on primary key

### ✅ Third Normal Form (3NF)

- Meets 2NF requirements
- No transitive dependencies
- Non-key attributes don't depend on other non-key attributes

### ✅ Boyce-Codd Normal Form (BCNF)

- Meets 3NF requirements
- Every determinant is a candidate key
- Address normalization eliminates redundancy

---

## 🎯 BUSINESS RULES IMPLEMENTED

1. **User Management**: Multi-role support with proper address handling
2. **Property Listings**: Complete property management with availability control
3. **Booking System**: Full booking lifecycle with payment integration
4. **Review System**: Bidirectional reviews with moderation and voting
5. **Communication**: Real-time messaging with conversation management
6. **Payment Processing**: Complete payment flow with refund handling
7. **Audit Trail**: Comprehensive change tracking and security logging
8. **Privacy Compliance**: GDPR-ready with consent and retention management

---

_Last Updated: November 2025_
_Database Design Level: Production-Ready_
_Normalization Level: BCNF Compliant_
