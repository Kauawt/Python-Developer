document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://127.0.0.1:8000'; // URL base da sua API FastAPI

    // Seções da UI
    const loginSection = document.getElementById('login-section');
    const mainSection = document.getElementById('main-section');
    const createAccountSection = document.getElementById('create-account-section');
    const createAccountForm = document.getElementById('create-account-form');

    // Forms
    const loginForm = document.getElementById('login-form');
    const transactionForm = document.getElementById('transaction-form');

    // Botões
    const showCreateAccountBtn = document.getElementById('show-create-account-btn');
    const logoutButton = document.getElementById('logout-button');

    // Elementos de Exibição
    const accountInfo = document.getElementById('account-info');
    const statementList = document.getElementById('statement-list');

    let token = null;
    let currentAccountId = null;
    let currentUserId = null;
    let currentUsername = localStorage.getItem('username') || '';

    //------------------------------------------------------------------
    // FUNÇÕES AUXILIARES
    //------------------------------------------------------------------

    const showLogin = () => {
        loginSection.classList.remove('hidden');
        createAccountSection.classList.remove('hidden');
        mainSection.classList.add('hidden');
        token = null;
        currentAccountId = null;
        currentUserId = null;
        localStorage.removeItem('authToken');
        localStorage.removeItem('accountId');
        localStorage.removeItem('userId');
        localStorage.removeItem('username');
        currentUsername = '';
    };

    const showApp = () => {
        loginSection.classList.add('hidden');
        createAccountSection.classList.add('hidden');
        mainSection.classList.remove('hidden');
    };

    //------------------------------------------------------------------
    // LÓGICA DA APLICAÇÃO
    //------------------------------------------------------------------

    // Função para decodificar JWT (sem verificação de assinatura)
    const decodeJWT = (token) => {
        try {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));
            return JSON.parse(jsonPayload);
        } catch (error) {
            console.error('Erro ao decodificar JWT:', error);
            return null;
        }
    };

    // Evento de Login
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (!username || !password) {
            alert('Por favor, preencha todos os campos.');
            return;
        }

        try {
            // 1. Fazer login para obter o token
            const loginResponse = await fetch(`${API_URL}/auth/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            if (!loginResponse.ok) {
                throw new Error('Falha no login. Verifique o usuário e senha.');
            }

            const loginData = await loginResponse.json();
            token = loginData.access_token;
            localStorage.setItem('authToken', token);

            // 2. Extrair user_id do token JWT
            const tokenPayload = decodeJWT(token);
            if (!tokenPayload || !tokenPayload.sub) {
                throw new Error('Token inválido.');
            }
            
            currentUserId = parseInt(tokenPayload.sub);
            localStorage.setItem('userId', currentUserId);
            localStorage.setItem('username', username);
            currentUsername = username;

            // 3. Buscar a conta associada ao user_id
            const accountsResponse = await fetch(`${API_URL}/accounts/?limit=100`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (!accountsResponse.ok) {
                throw new Error('Não foi possível buscar as contas.');
            }

            const accounts = await accountsResponse.json();
            const userAccount = accounts.find(acc => acc.user_id === currentUserId);

            if (!userAccount) {
                throw new Error('Nenhuma conta encontrada para este usuário.');
            }

            currentAccountId = userAccount.id;
            localStorage.setItem('accountId', currentAccountId);

            // 4. Exibir a aplicação
            showApp();
            await loadAccountData();

        } catch (error) {
            alert(`Erro: ${error.message}`);
            showLogin();
        }
    });

    // Mostrar/Ocultar formulário de criação de conta
    showCreateAccountBtn.addEventListener('click', () => {
        createAccountForm.classList.toggle('hidden');
    });

    // Evento de Criar Conta
    createAccountForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = document.getElementById('new-username').value;
        const password = document.getElementById('new-password').value;
        const initialBalance = parseFloat(document.getElementById('initial-balance').value);

        if (!username || !password) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        if (isNaN(initialBalance) || initialBalance < 0) {
            alert('Por favor, insira um saldo inicial válido.');
            return;
        }

        try {
            // 1. Criar usuário
            const userResponse = await fetch(`${API_URL}/auth/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!userResponse.ok) {
                const errorData = await userResponse.json();
                throw new Error(errorData.detail || 'Falha ao criar usuário.');
            }

            const newUser = await userResponse.json();

            // 2. Fazer login para obter token
            const loginResponse = await fetch(`${API_URL}/auth/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            if (!loginResponse.ok) {
                throw new Error('Falha no login após criação do usuário.');
            }

            const loginData = await loginResponse.json();
            token = loginData.access_token;

            // 3. Criar conta bancária
            const accountResponse = await fetch(`${API_URL}/accounts`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({ 
                    user_id: newUser.id, 
                    balance: initialBalance 
                }),
            });

            if (!accountResponse.ok) {
                const errorData = await accountResponse.json();
                throw new Error(errorData.detail || 'Falha ao criar conta bancária.');
            }

            const newAccount = await accountResponse.json();
            
            alert(`Conta criada com sucesso! Use o usuário "${username}" para fazer login.`);
            createAccountForm.reset();
            createAccountForm.classList.add('hidden');

        } catch (error) {
            alert(`Erro: ${error.message}`);
        }
    });

    // Evento de Criar Transação
    transactionForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const type = document.getElementById('tx-type').value;
        const amountInput = document.getElementById('tx-amount');
        const amount = parseFloat(amountInput.value);

        if (isNaN(amount) || amount <= 0) {
            alert('Por favor, insira um valor válido.');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/transactions`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({
                    account_id: currentAccountId,
                    type: type,
                    amount: amount,
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Falha ao criar transação.');
            }

            // Recarrega os dados da conta para mostrar o saldo atualizado e a nova transação
            await loadAccountData();
            transactionForm.reset();

        } catch (error) {
            alert(`Erro: ${error.message}`);
        }
    });

    // Evento de Logout
    logoutButton.addEventListener('click', () => {
        showLogin();
    });

    const renderAccountInfo = (account) => {
        accountInfo.innerHTML = `
            <p><strong>Conta ID:</strong> ${account.id}</p>
            <p><strong>Nome de usuário:</strong> ${currentUsername}</p>
            <p><strong>Saldo:</strong> R$ ${parseFloat(account.balance).toFixed(2)}</p>
            <p><strong>Criada em:</strong> ${new Date(account.created_at).toLocaleString()}</p>
        `;
    };

    const renderTransactions = (transactions) => {
        statementList.innerHTML = '';
        if (transactions.length === 0) {
            statementList.innerHTML = '<p>Nenhuma transação encontrada.</p>';
            return;
        }
        transactions.forEach(tx => {
            const txType = tx.type === 'deposit' ? 'Depósito' : 'Saque';
            const txColor = tx.type === 'deposit' ? 'text-green-600' : 'text-red-600';
            const txElement = document.createElement('div');
            txElement.className = 'p-2 border-b';
            txElement.innerHTML = `
                <div class="flex justify-between">
                    <span>${txType}</span>
                    <span class="${txColor}">R$ ${parseFloat(tx.amount).toFixed(2)}</span>
                </div>
                <div class="text-sm text-gray-500">${new Date(tx.timestamp).toLocaleString()}</div>
            `;
            statementList.appendChild(txElement);
        });
    };

    const loadAccountData = async () => {
        if (!token || !currentAccountId) return;

        try {
            // Buscar todas as contas e filtrar a atual
            const accountsResponse = await fetch(`${API_URL}/accounts/?limit=100`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            if (!accountsResponse.ok) throw new Error('Falha ao carregar dados da conta.');
            const accounts = await accountsResponse.json();
            const account = accounts.find(acc => acc.id === currentAccountId);
            
            if (!account) {
                throw new Error('Conta não encontrada.');
            }
            
            renderAccountInfo(account);

            // Buscar extrato (transações)
            const transactionsResponse = await fetch(`${API_URL}/accounts/${currentAccountId}/transactions?limit=100`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            if (!transactionsResponse.ok) throw new Error('Falha ao carregar extrato.');
            const transactions = await transactionsResponse.json();
            renderTransactions(transactions);

        } catch (error) {
            alert(`Erro: ${error.message}`);
            showLogin();
        }
    };

    //------------------------------------------------------------------
    // INICIALIZAÇÃO
    //------------------------------------------------------------------
    const init = async () => {
        token = localStorage.getItem('authToken');
        currentAccountId = localStorage.getItem('accountId');
        currentUserId = localStorage.getItem('userId');

        if (token && currentAccountId && currentUserId) {
            showApp();
            await loadAccountData();
        } else {
            showLogin();
        }
    }

    init();
}); 